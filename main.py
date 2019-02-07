import json
from pprint import pprint
import xml.etree.ElementTree as ET

words = []
with open("newsafr.json") as newsafr_file:
    movie = json.load(newsafr_file)
    i = 0
    while i < len(movie["rss"]["channel"]["items"]):
      i2 = 0
      while i2 < len(movie["rss"]["channel"]["items"][i]["description"].split(" ")):
        if not movie["rss"]["channel"]["items"][i]["description"].split(" ")[i2] in words:
          words.append(movie["rss"]["channel"]["items"][i]["description"].split(" ")[i2])
        i2 += 1
      i += 1

words_sort = sorted(words, key=len)
words_sort_reverse = words_sort.reverse()

i = 1
while i <= 10:
  print(str(i) + ".", words_sort[i])
  i += 1

# ==============================

tree = ET.parse("newsafr.xml")
root = tree.getroot()
print(root.tag)