import re

"""
Regular Expressions: matching text, based on a pre-defined pattern. It can detect the presence or absence of a text 
by matching with a particular pattern, and also can split a pattern into one or more sub-patterns

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

# ______________________________ code begins __________________________________________________
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

123*555*1234

abcdefgh

800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
hat 
mat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
# pattern = re.compile(r"\d{3}.\d{3}.\d{4}")  # {no_of_digits} specifies the amount of digits

# pattern = re.compile(r"Mr\.?\s[A-Z]\w*")  # ? means 0 or one times. \w-Word Character (a-z, A-Z, 0-9, _)
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")  # ? means 0 or one times. \w-Word Character (a-z, A-Z, 0-9, _)

# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d")
# pattern = re.compile(r"[a-zA-Z]+")
# pattern = re.compile(r"[^a-zA-Z]")  # negates the search and matches everything outside the search
# pattern = re.compile(r"[^b]at")  # search for anything that's not a 'b', followed by a literal 'at'

# finditer: returns (an iterable) all the matches with extra functions such as 'group()' and index of the search
# matches = pattern.finditer(text_to_search)

matches = pattern.findall(text_to_search)  # findall: returns (an iterable) only the match without extra functions
# .match(): returns (no iterable) the first match at the beginning of the sentence or phrase. Returns None if no match
# .search(): returns (no iterable) the first match within the sentence or phrase. Returns None if no match

# with open('data.txt', 'r') as f:
#     contents = f.read()
#
#     matches = pattern.finditer(contents)

for match in matches:
    print(match)
    # print("{} -> {}".format(match, match.group()))
