#fintxer recommends using archived freelance requests in the $0-50 range to practice Python skills
#https://www.freelancer.com/projects/python/need-python-programmer-familiar-with-27775329/?ngsw-bypass=&w=f

import urllib.request
import re
import json

f = open("pg1041.txt", "r")
ebook = f.read()
pattern = re.compile('The Project Gutenberg EBook of ([^,]*), by ([\w ]*)$', re.MULTILINE)
m = pattern.search(ebook)
ebook_dict = {}
ebook_dict['Title:'] = m.group(1)
ebook_dict['Author:'] = m.group(2)

pattern = re.compile('Last Updated: .*', re.MULTILINE)
m = pattern.search(ebook)
ebook_dict['last updated'] = m.group()

#https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
#roman_numeral_pattern = '^^  (CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$$'
sonnet_pattern = r"\n\n  ([IVXLCDM]{1,8})\n\n((?: {2,4}.*\n{1,1})+(?: {2,4}.*(?=\n{2,3})))"
pattern = re.compile(sonnet_pattern, re.MULTILINE)
sonnets = pattern.findall(ebook)

sonnet_list = []
for sonnet in sonnets:
    sonnet_dict = {}
    sonnet_dict["number"] = sonnet[0]
    sonnet_dict["lines"] = sonnet[1]
    sonnet_list.append(sonnet_dict)

ebook_dict['sonnets'] = sonnet_list

with open('data.txt', 'w') as outfile:
    json.dump(ebook_dict, outfile, indent=1)
