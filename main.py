import json
from pprint import pprint
import xml.etree.ElementTree as ET

words = []
words_list = []
words_count = []
with open("newsafr.json") as newsafr_file:
    movie = json.load(newsafr_file)
    i = 0
    while i < len(movie["rss"]["channel"]["items"]):
      i2 = 0
      while i2 < len(movie["rss"]["channel"]["items"][i]["description"].split(" ")):
        if not movie["rss"]["channel"]["items"][i]["description"].split(" ")[i2] in words:
          words.append(movie["rss"]["channel"]["items"][i]["description"].split(" ")[i2])
        words_list.append(movie["rss"]["channel"]["items"][i]["description"].split(" ")[i2])
        i2 += 1
      i += 1

for word in words:
  words_count.append({"word": word, "count": words_list.count(word)})

words_sorted = sorted(words_count, key=lambda x: x['count'], reverse=True)

print_list = []
for item in words_sorted:
  if len(item["word"]) >= 6:
    print_list.append({"word": item["word"], "count": item["count"]})
  if len(print_list) == 10:
    break

for word in print_list:
  print(word["word"], "-", word["count"])

print("\n")

# ==============================

parser = ET.XMLParser(encoding = 'utf-8')

words_xml = []
words_list_xml = []
words_count_xml = []
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item/description")
for xmli in xml_items:
  i = 0
  while i < len(xmli.text.split(" ")):
    words_list_xml.append(xmli.text.split(" ")[i])
    if not xmli.text.split(" ")[i] in words_xml:
      words_xml.append(xmli.text.split(" ")[i])
    i += 1

for word in words_xml:
  words_count_xml.append({"word": word, "count": words_list_xml.count(word)})

words_sorted_xml = sorted(words_count_xml, key=lambda x: x['count'], reverse=True)

print_list_xml = []
for item in words_sorted_xml:
  if len(item["word"]) >= 6:
    print_list_xml.append({"word": item["word"], "count": item["count"]})
  if len(print_list_xml) == 10:
    break

for word in print_list_xml:
  print(word["word"], "-", word["count"])
