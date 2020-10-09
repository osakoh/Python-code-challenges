import re

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

pattern = re.compile(r'start', re.I)  # the flag(IGNORECASE/I) ignores the case

# .match(): returns (no iterable) the first match at the beginning of the sentence or phrase. Returns None if no match
matches = pattern.match(sentence)

print(matches)
