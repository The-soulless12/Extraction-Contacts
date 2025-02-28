# Extraction-Contacts
Extraction des e-mails, numéros de téléphone et liens vers les réseaux sociaux à partir de sites web, implémentée en Python et utilisant des expressions régulières (Regex) afin d'unifier les formats.

# Fonctionnalités 
- Extraction et normalisation des e-mails, numéros de téléphone et liens vers les réseaux sociaux.

# Structure du projet
- main.py : Point d'entrée du programme, gère l'exécution et l'affichage des résultats.
- contacts.py : Contient les expressions régulières qui normalisent les données.
- validation/ : Contient les fichiers HTML des sites web.
- test/ : Contient les tests unitaires afin de valider la robustesse des regex.

# Prérequis
- Python version 3.x

# Note
- Pour exécuter le projet, saisissez la commande `python main.py validation/` ou `python main.py test/` dans votre terminal.
