__author__ = 'hatem'
import re

enchere = list()
temp = list()
with open("in101.txt", "r") as f_handler:
    for line in f_handler:
        line = line.lstrip()
        find = re.search("([0-9]+.*)\s*", line)
        if find is not None:
            offre = find.group(1)
            offre = offre.split()
            price = float(offre[0])
            offre.pop(0)
            temp = [price, offre]
            enchere.append(temp)
# print enchere
items = list()

for handler in enchere:
    items.append(handler[1])

#print items

def where_not_exists(item, items):
    buff = list()
    for it in items:
        if it != item:
            found = False
            for element in item:
                for elt in it:
                    if elt == element:
                        found = True
                        break
            if not found:
                buff.append(items.index(it))
    return buff

compatible = list()

for offre in items:
    compatible.append(where_not_exists(offre,items))
print compatible
print len(compatible)
