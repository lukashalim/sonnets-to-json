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

#[IVXLCDM]{1,8} does not perfectly identify roman numerals, but works for this purpose
#After the roman numeral, there are two line breaks before the sonnet text
#The lines of the sonnet have single line breaks, followed by multiple line breaks at the end
#this is captured by the pattern ((?: {2,4}.*\n)+(?: {2,4}.*(?=\n{2,3})))
sonnet_pattern = r"\n\n  ([IVXLCDM]{1,8})\n\n((?: {2,4}.*\n)+(?: {2,4}.*(?=\n{2,3})))"
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
