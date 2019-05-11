import re
import collections

# https://www.w3schools.com/python/python_regex.asp

text = open('book.txt').read().lower()
words = re.findall("th.",text)
print(collections.Counter(words).most_common(20))