# sonnets-to-json

I'm taking a Python course which recommends searching through archived Python projects on Freelancer.com and completing projects that suit your interest. I found this one https://www.freelancer.com/projects/python/need-python-programmer-familiar-with-27775329 which requested a python program to convert the [Gutenberg etext version](https://www.freelancer.com/users/l.php?url=http:%2F%2Fwww.gutenberg.org%2Fcache%2Fepub%2F1041%2Fpg1041.txt&sig=90214a17cbddc4105b4199da392ad6d76050586769512cef0a479afa3ad4a46e) of Shakepeae's sonnets to JSON format using regular expressions.

Most of the effort for this was finding a regular expression that would match format of the sonnets, which begin with a roman numeral for the sonnet number, followed by line breaks, followed by the sonnet text. I found it helpful to develop the pattern using a [RegEx tester](https://regex101.com/) with the Python option selected.
