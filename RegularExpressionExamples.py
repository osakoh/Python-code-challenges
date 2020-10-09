import re

"""
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-z-]+\.(com|edu|net)')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print("{} -> {}".format(match, match.group()))
"""

"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One (optional)
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
"""
# Fully Qualified Domain Name(FQDN) = [hostname].[domain name].[top level domain(tld)]
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# 4 groups below:
# group 0 - the Fully Qualified Domain Name(FQDN)
# group 1 - hostname
# group 2 - domain name
# group 3 - top level domain

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.finditer(urls)

# for match in matches:
#     print("{} -> {}".format(match, match.group(3)))

subbed_urls = pattern.sub(r'\2\3', urls)  # back references \2\3 i.e group 2&3

print(subbed_urls)

# for match in matches:
#     print("{} -> {}".format(match, match.group(3)))