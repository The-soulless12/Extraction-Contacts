import re

mails = [
    (re.compile(r'([\w.-]+)@([\w.-]+)\.(\w+)'), '$1@$2.$3')
]

socials = [
    (re.compile(r'https?://(?:www\.)?facebook\.com/(?!sharer)(([^/"\s?])+)'), 'facebook:$1'),
    (re.compile(r'https?://(?:www\.)?instagram\.com/(([^/"\s?])+)'), 'instagram:$1'),
    (re.compile(r'https?://(?:www\.)?twitter\.com/(?!intent|home)(([^/"\s?])+)'), 'twitter:$1'),
    (re.compile(r'https?://(?:www\.)?youtube\.com/channel/(([^/"\s?])+)'), 'youtube:$1'),
    (re.compile(r'https?://(?:www\.)?linkedin\.com/company/(([^/"\s?])+)'), 'linkedin:$1')
]

tels = [
    # Format : (0xx)(.- )xx(.- )xx(.- )xx && (0 xx)(.- )xx(.- )xx(.- )xx && 0xx(.- )xx(.- )xx(.- )xx && 0 xx(.- )xx(.- )xx(.- )xx
    (re.compile(r'\(?(0)\s*(\d{2})\)?(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$2) $3 $4 $5'),
    # Format : xxx(.- )xx(.- )xx|x(.- )x|xx
    (re.compile(r'(\d{3})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(\d{1})(?:\s+|\.|-)+(\d{1})(\d{2})'), '(0$2) $3 $4$5 $6'),
    # Format : tel:xxxxxxxxx && fax:xxxxxxxxx
    (re.compile(r'(tel\s*:\s*|Tel\s*:\s*|tél\s*:\s*|Tél\s*:\s*|Fax\s*:\s*|fax\s*:\s*)(\d{3})(\d{2})(\d{2})(\d{2})'), '($2) $3 $4 $5'),
    # Format : +( )xxx(.- )xx(.- )xx(.- )xx(.- )xx && [parenthèse autour de xxx]
    (re.compile(r'(\+)\s*\(?(\d{3})\)?(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)*(\d{2})'), '(0$3) $4 $5 $6'),
    # Format : +xxx(.- )(x)(.- )xx(.- )xx(.- )xx(.- )xx && [+ non obligatoire] && [parenthèse facultatives autour du xxx]
    (re.compile(r'(\+)?\(?(\d{3})\)?(?:\s+|\.|-)+(\(\d\))(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$4) $5 $6 $7'),
    # Format : (xxx)(.- )xx(.- )xx(.- )xx(.- )xx
    (re.compile(r'\((\+*\d{3})\)(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})'), '(0$2) $3 $4 $5'),
    # Format : Cas des numéros avec "ou" (3 ou de suite pris en charge seulement)
    (re.compile(r'\d{3}(?:\s+|\.|-)+\(\d\)*(?:\s+|\.|-)*(\d{2})*(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(ou\s+)(\d{2})'), '(0$1) $2 $3 $6'),
    (re.compile(r'\d{3}(?:\s+|\.|-)+\(\d\)*(?:\s+|\.|-)*(\d{2})*(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(ou\s+)(\d{2})(?:\s+|\.|-)+(ou\s+)(\d{2})'), '(0$1) $2 $3 $8'),
    (re.compile(r'\d{3}(?:\s+|\.|-)+\(\d\)*(?:\s+|\.|-)*(\d{2})*(?:\s+|\.|-)*(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(\d{2})(?:\s+|\.|-)+(ou\s+)(\d{2})(?:\s+|\.|-)+ou\s+(\d{2})(?:\s+|\.|-)+ou\s+(\d{2})'), '(0$1) $2 $3 $8'),
]
