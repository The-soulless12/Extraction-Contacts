import re

mails = [
    (re.compile(r'(\w+)@(\w+)\.(\w+)'), '$1@$2.$3')
]

socials = [
    (re.compile(r'https?://(?:www\.)?facebook\.com/(?!sharer)(([^/"\s?])+)'), 'facebook:$1'),
    (re.compile(r'https?://(?:www\.)?instagram\.com/(([^/"\s?])+)'), 'instagram:$1'),
    (re.compile(r'https?://(?:www\.)?twitter\.com/(?!intent)(([^/"\s?])+)'), 'twitter:$1'),
    (re.compile(r'https?://(?:www\.)?youtube\.com/channel/(([^/"\s?])+)'), 'youtube:$1'),
    (re.compile(r'https?://(?:www\.)?linkedin\.com/company/(([^/"\s?])+)'), 'linkedin:$1')
]

tels = [
    # Format : (0xx)(.- )xx(.- )xx(.- )xx && (0 xx)(.- )xx(.- )xx(.- )xx && 0xx(.- )xx(.- )xx(.- )xx && 0 xx(.- )xx(.- )xx(.- )xx
    (re.compile(r'\(?(0)\s*(\d{2})\)?(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$2) $3 $4 $5'),
    # Format : xxx(.- )xx(.- )xx|x(.- )x|xx
    (re.compile(r'(\d{3})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(\d{1})(?:\s+|\.|-)+(\d{1})(\d{2})'), '(0$2) $3 $4$5 $6'),
    # Format : tel:xxxxxxxxx 
    (re.compile(r'(tel:)(\d{3})(\d{2})(\d{2})(\d{2})'), '($2) $3 $4 $5'),
    # Format : +xxx(.- )xx(.- )xx(.- )xx(.- )xx
    (re.compile(r'(\+\d{3})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$2) $3 $4 $5'),
    # Format : +xxx(.- )x(.- )xx(.- )xx(.- )xx(.- )xx && +xxx(.- )(x)(.- )xx(.- )xx(.- )xx(.- )xx && [+ non obligatoire] && [parenthèse facultatives autour du xxx]
    (re.compile(r'(\+)?\(?(\d{3})\)?(?:\s+|\.|-)+(\(\d\))+(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$4) $5 $6 $7')
]

"""Notes : 
caar : le cas des ou
          (021) 63 20 73  :  sys(0), ref(4)
          (021) 63 20 88  :  sys(0), ref(4)
          (021) 63 20 55  :  sys(0), ref(4) ---> 213 (0)21 63 20 72 ou 73 ou 88 ou 55  

asal :
(023) 27 05 31  :  sys(0), ref(1)
          (023) 27 05 24  :  sys(0), ref(1)

algerietelecom :
(021) 82 38 38  :  sys(0), ref(1)
          (021) 82 38 39  :  sys(0), ref(1)
          (021) 78 88 01  :  sys(0), ref(1)
"""
