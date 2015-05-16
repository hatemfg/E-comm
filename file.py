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

def heuristic(items, enchere):
    """

    :param items:
    :param enchere:
    :return:
    """

    weights = list()
    max_items = 0
    max_prix = 0
    min_items = len(items[0])
    min_prix = enchere[0][0]

    for i in range(0, len(items)):
        if len(items[i]) > max_items:
            max_items = len(items[i])

        if len(items[i]) < min_items:
            min_items = len(items[i])

        if enchere[i][0] > max_prix:
            max_prix = enchere[i][0]

        if enchere[i][0] < min_prix:
            min_prix = enchere[i][0]

    for i in range(0, len(items)):
        temp_items = (float(max_items ))/ (len(items[i]) )
        temp_prix = (enchere[i][0] ) / (float(max_prix ))
        #print temp_prix,temp_items
        weight = temp_items + float(temp_prix)
        weights.append(weight)
    return weights

def random_Key(items):
    """

    :param items: list of offers
    :return: list of randomKeys
    """
    RK = list()
    for i in range(0, len(items)):
        rnd = random.random()
        rnd = round(rnd,2)
        RK.append(rnd)
    return RK



def heuristic_sample(A):
    B = list()
    for i in range(0,len(A)):
        B.append([A[i],None,None])
    return B

def maximum_list_list(A):
    max = 0
    indice_max = -1

    for i in range(0,len(A)):
        if( max <= A[i][0]):
            max = A[i][0]
            indice_max = A.index(A[i])

    return indice_max

def trier_offres(A):
    """

    :rtype : List if list
    """
    B = list()
    A.sort(reverse = True)

    for i in range(0,len(A)):
        B.append([A[i],i])
    return B

def Heuristic_algorithm(items,enchere,incompatible,max_iter):
    RK = list()
    A = list()
    nb_itemsMax = 0
    priceMax = 0

    for i in range(0,max_iter):
        price  = 0
        nb_items = 0
        RK = heuristic(items,enchere)
        A = RK[:]
        empty = True

        already_assigned = list()
        for i in range(0,len(A)):
            already_assigned.append(1)

        while empty:
            offer = random.randint(0,len(A)-1)
            if A[offer] != 0:
                empty = False
                already_assigned[offer] = 0

        temp = incompatible[offer]
        for j in range(0,len(temp)):
            already_assigned[temp[j]] = -1

        cpt = 0
        C = trier_offres(A)

        while cpt < len(A):
            j = 0
            B = C[:]
            price = 0
            nb_items = 0

            while max(already_assigned) != 0:
                while ((already_assigned[j] <= 0) and (j < len(A))):
                    j += 1
                already_assigned[j] = 0
                temp = incompatible[j]
                for k in range(0,len(temp)):
                    already_assigned[temp[k]] = -1

            for k in range(0,len(B)):
                if int(already_assigned[k]) == int(0):
                    price = price + enchere[C[k][1]][0]

            if (price > priceMax) :
                priceMax = price
                toto = already_assigned
            cpt += 1

    return priceMax,nb_itemsMax

def random_copie(items,A):
    RK = list()
    for i in range(0,len(items)):
        if ((int(A[i]) != int(0)) and (int(A[i]) != int(-1))):
            rnd = random.random()
            rnd = round(rnd,2)
            RK.append(rnd)
        else :
            RK.append(A[i])

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
            offer = A.index(max(A))
            if A[offer] != 0:
                empty = False
                A[offer] = 0

        temp = incompatible[offer]
        for j in range(0,len(temp)):
            A[temp[j]] = -1
        cpt = 0
        while cpt < 3 :
            price = 0
            nb_items = 0
            B = random_copie(items,A)
            while True:
                j = B.index(max(B))
                if max(B) == 0:
                    break
                B[j] = 0
                temp = incompatible[j]
                for k in range(0,len(temp)):
                    B[temp[k]] = -1

            for k in range(0,len(B)):
                if int(B[k]) == int(0):
                    price = price + enchere[k][0]
                    nb_items = nb_items + len(enchere[k][1])

            if (price > priceMax) :
                priceMax = price
                RES = B
            cpt += 1

    return priceMax,nb_itemsMax,RES
#print enchere
#print items
#print heuristic(items, enchere)
print Heuristic_algorithm(items,enchere,incompatible,100)


