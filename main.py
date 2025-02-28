import re
import os
import sys
from typing import List, Dict

from contacts import mails, socials, tels

regs = {
    'mails'   : mails,
    'socials' : socials,
    'tels'    : tels
}

# Extrait les adresses e-mail, réseaux sociaux et numéros de téléphone à partir d'un fichier HTML
def process_file(url: str) -> Dict[str, List[str]]:
    result = {
        'mails'   : [],
        'socials' : [],
        'tels'    : []
    }

    f = open(url, 'r')
    for l in f:
        for type in regs:
            for reg, pattern in regs[type]:
                ms = reg.findall(l)
                for m in ms:
                    content = pattern
                    for j in range(len(m)):
                        content = content.replace('$' + str(j+1), m[j])
                    result[type].append(content)
    f.close()
    return result

# Calcule la fréquence de chaque élément
def process_stats(lst: List[str]) -> Dict[str, int]:
    stats = {}
    for e in lst:
        if not e in stats:
            stats[e] = 0
        stats[e] += 1
    return stats

# Traite tous les fichiers HTML d'un dossier donné
def process_folder(url: str) -> Dict[str, Dict[str, List[Dict[str, int]]]]:
    contacts = {}
    for name_f in os.listdir(url):
        m = re.match(r'^([^.].*)\.html$', name_f)
        if m:
            title = m[1]
        else:
            continue
        url_f = os.path.join(url, name_f)
        result = process_file(url_f)
        contact = {
            'mails'   : process_stats(result['mails']),
            'socials' : process_stats(result['socials']),
            'tels'    : process_stats(result['tels'])
        }
        contacts[title] = contact
    return contacts

# Traite le fichier de référence
def process_reference(url: str):
    contacts = {}
    f = open(url, 'r')
    for l in f:
        info = l.split("	")
        if len(info) < 4:
            continue
        if not info[0] in contacts:
            contacts[info[0]] = {
                'mails'   : {},
                'socials' : {},
                'tels'    : {}
            }
        contacts[info[0]][info[1]][info[2]] = int(info[3])
    f.close()
    return contacts

# Évalue la précision des données extraites par rapport à la référence
def evaluate(sys_contacts, ref_contacts):
    INT = 0  # Intersection entre la référence et les résultats extraits
    SYS = 0  # Nombre total d'éléments extraits
    REF = 0  # Nombre total d'éléments dans la référence
    resultat = {}

    for fichier in ref_contacts:
        resultat[fichier] = {}

        ref_types = ref_contacts[fichier]
        if fichier in sys_contacts:
            sys_types = sys_contacts[fichier]
        else:
            sys_types = None

        for type in ['mails', 'socials', 'tels']:
            res_elements = resultat[fichier][type] = {}
            for element in ref_types[type]:
                ref_nbr = ref_types[type][element]
                sys_nbr = 0
                if (sys_types is not None) and (element in sys_types[type]):
                    sys_nbr = sys_types[type][element]
                res_elements[element] = 'sys(' + str(sys_nbr) + '), ref(' + str(ref_nbr) + ')'
                SYS += sys_nbr
                REF += ref_nbr
                INT += min(sys_nbr, ref_nbr)
            if sys_types:
                for element in sys_types[type]:
                    if element not in res_elements:
                        sys_nbr = sys_types[type][element]
                        res_elements[element] = 'sys(' + str(sys_nbr) + '), ref(0)'
                        SYS += sys_types[type][element]

    R = INT / REF
    P = 0.0 if SYS == 0 else INT / SYS
    F1 = 0.0 if R + P == 0 else 2 * P * R / (P + R)
    return resultat, R, P, F1

# Affiche les statistiques des contacts extraits
def printing(contacts):
    for fichier in contacts:
        print('========== ', fichier, ' ==========') 
        stats = contacts[fichier]
        for type in stats:
            print('------> ', type)
            stats_type = stats[type]
            for element in stats_type:
                print('         ', element, ' : ', stats_type[element])

if __name__ == '__main__':
    url = './'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    sys_contacts = process_folder(url)
    ref_contacts = process_reference(os.path.join(url, 'ref.txt'))
    comp, R, P, F1 = evaluate(sys_contacts, ref_contacts)
    printing(comp)
    print('---------------------------------------------------')
    print('R =', R, ', P =', P, ', F1 =', F1)