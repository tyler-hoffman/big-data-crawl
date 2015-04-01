#!/usr/bin/python

import re
import sys

# regex for html body; the contents will be extracted
body_pattern = re.compile('<body.*?>(.*?)</body>', re.DOTALL)

# regex for javascript and html tags
script_pattern = re.compile('(<script.*?</script>)|(<noscript*?</noscript>)', re.DOTALL)
html_pattern = re.compile('(<!--.*?-->)|(<.*?>)', re.DOTALL)

# regex for various characters, etc. that I don't want to see
nonword_pattern = re.compile(r'(&.+?;)|\\|\.\s|\||\"|!|:|;|,|/', re.DOTALL)

# read input (use file redirection)
html = sys.stdin.read()

# get the body
body = re.search(body_pattern, html).group(1);

# get rid of html tags and other unwanted stuff
cleaned = re.sub(script_pattern, '', body)
cleaned = re.sub(html_pattern, ' ', cleaned)
cleaned = re.sub(nonword_pattern, ' ', cleaned)

# get all the words from the cleaned text and display them
words = cleaned.split()
for word in words:
	print word

