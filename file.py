__author__ = 'hatem'
import re
import random
from decimal import *

enchere = list()
temp = list()
incompatible = list()
items = list()

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

for handler in enchere:
    items.append(handler[1])


def where_exists(item,items):
    """
    a function generating a list of incompatible offers

    :param item: offer
    :param items: a list of offers
    :return: a list of incompatible offers
    """
    buff = list()
    for it in items:
        if it != item:
            found = False
            for element in item:
                for elt in it:
                    if elt == element:
                        found = True
                        break
            if found:
                buff.append(items.index(it))
    return buff


for offre in items:
    incompatible.append(where_exists(offre,items))


def random_Key(items):
    RK = list()
    for i in range(0,len(items)):
        rnd = random.random()
        rnd = round(rnd,2)
        RK.append(rnd)
    return RK

def SLS_algorithm(items,enchere,incompatible,max_iter):
    RK = list()
    A = list()
    nb_itemsMax = 0
    priceMax = 0

    for i in range(0,max_iter):
        price  = 0
        nb_items = 0
        RK = random_Key(items)
        A = RK[:]
        r = random.random()
        empty = True

        while empty:
            if r < 0.2:
                offer = random.randint(0,len(A)-1)
            else :
                offer = A.index(max(A))
            if A[offer] != 0:
                empty = False
                A[offer] = 0

        temp = incompatible[offer]
        for j in range(0,len(temp)):
            A[temp[j]] = -1

        while True:
            j = A.index(max(A))
            if max(A) == 0:
                break
            A[j] = 0
            temp = incompatible[j]
            for k in range(0,len(temp)):
                A[temp[k]] = -1

        for k in range(0,len(A)):
            if A[k] == 0:
                price = price + enchere[k][0]
                nb_items = nb_items + len(enchere[k][1])

        if (price > priceMax) :
            priceMax = price

    return priceMax,nb_itemsMax



print SLS_algorithm(items,enchere,incompatible,1000)


