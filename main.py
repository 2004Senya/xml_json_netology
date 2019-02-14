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
words_sort.reverse()

i = 1
while i <= 10:
  print(str(i) + ".", words_sort[i])
  i += 1

print("\n")
# ==============================

parser = ET.XMLParser(encoding = 'utf-8')

words_xml = []
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item/description")
for xmli in xml_items:
  i = 0
  while i < len(xmli.text.split(" ")):
    if not xmli.text.split(" ")[i] in words_xml:
      words_xml.append(xmli.text.split(" ")[i])
    i += 1

words_sort_xml = sorted(words_xml, key=len)
words_sort_xml.reverse()

i = 1
while i <= 10:
  print(str(i) + ".", words_sort_xml[i])
  i += 1
