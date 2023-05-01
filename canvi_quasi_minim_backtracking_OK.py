# pseudocodi
# el que podem fer és calcular el canvi mínim i després fer el len de la resposta que ens dona i comparar
import math
from pytokr import items, item 

def canvi_minim_resposta_1604(e,monedes=[1,2,5,10,20,50,100,200]): 
    quantitat = e
    opcions = sorted(monedes, reverse = True)
    i = 0
    llista_respostes = []
    while quantitat != 0 and i<len(opcions):
        if opcions[i] <= quantitat: 
            llista_respostes.append(opcions[i])
            quantitat = round(quantitat-opcions[i],2)
        else: 
            i += 1 
    if quantitat == 0: 
        return llista_respostes

def canvi_quasi_minim(canvi, monedes_utilitzades): 
    len_minim = len(canvi_minim_resposta_1604(canvi))
    if len(monedes_utilitzades) - len_minim <= 1: 
        print('si')
    else: 
        print('no')

def input(): 
    n = int(item())
    llista = list()
    for _ in range(n): 
        llista.append(int(item()))

    return n, llista 

while True: 
    try: 
        n, llista = input()
        
        canvi_quasi_minim(sum(llista),llista)
    except: 
        break 

