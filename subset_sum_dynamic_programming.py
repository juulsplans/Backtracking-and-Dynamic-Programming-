from pytokr import item, items 
from multiset import *
from collections import Counter
import math 

def suma_minima(suma, llista): 
    taula = [[None for i in range(suma+1)] for j in range(len(llista))]
    for i in range(len(llista)): 
        taula[i][0] = True 
    # primera iteració 

    for row in range(len(taula)): # OK
        for column in range(1,len(taula[0])): # OK
            if row == 0: 
                # si estem a la primera fila, vol dir que només tenim un element i per tant
                # només podem posar True a aquella columna que tingui el mateix número que la fila 
                for column in range(1,len(taula[0])): 
                    if column == llista[row]: 
                        taula[row][column] = True 
                    else: 
                        taula[row][column] = False

            else: 
                if column < llista[row]: 
                    taula[row][column] = taula[row-1][column] 
                else: # column >= llista[row]
                    if taula[row-1][column] == True: 
                        taula[row][column] = True
                    else: 
                        taula[row][column]= taula[row-1][column-llista[row]]
    for i in taula: 
        print(i)

    valor_final = taula[len(llista)-1][suma]
    if valor_final == True: 
        # buscar quin són els elements que ho fan possible 
        def aux(fila = (len(llista)-1), columna = suma, resultat = []): 
            if columna == 0 or fila == 0: #hem arribat al principi de la taula 
                return resultat
            elif taula[fila-1][columna] == True: # no afegim res
                return aux(fila-1,columna,resultat)
            else: # el true no ve del true de dalt 
                resultat.append(llista[fila])
                return aux(fila-1,columna-llista[fila],resultat[:])
        
        return aux()
        
    else: 
        return []    



def subset_sum_interval(L,U,llista): 
    subsets = []
    for i in range(L,U): 
        subsets.append(suma_minima(i,llista))
    print(subsets)

#subset_sum_interval(96,104,[60, 15, 25, 95, 80, 5, 10, 5, 10, 75])
# EL DE DALT NO VA, ANEM A PROVAR AMB UN ALTRE
from pytokr import item, items 

def sumes_iguals_1904(suma,n,llista): 
    def backtrack(i,suma,final_l,curr_l = []): 
        if suma == 0 and i!= 0 and curr_l not in final_l: 
            final_l.append(curr_l)  
            return 
        while i < n: 
            if llista[i] <= suma: 
                curr_l_cp = [x for x in curr_l] + [llista[i]]
                backtrack(i+1,suma-llista[i],final_l,curr_l_cp)
                backtrack(i+1,suma,final_l,curr_l)
                i += 1
            else: 
                backtrack(i+1,suma,final_l,curr_l)
                i += 1
        return 
    llista_respostes = []
    backtrack(0,suma,llista_respostes)
    minim_len = math.inf
    resposta_minima = None
    for i in llista_respostes: 
        if len(i) < minim_len: 
            resposta_minima = i
            minim_len = len(resposta_minima)
    return resposta_minima


def subset(L,U,llista): 
    llista_res = []
    for i in range(L,U): 
        resposta = sumes_iguals_1904(i,len(llista),llista)
        if resposta != None: 
            llista_res.append(sumes_iguals_1904(i,len(llista),llista))
    minim_len = math.inf 
    resposta_minima = None
    for i in llista_res: 
        if len(i) < minim_len: 
            resposta_minima = i
            minim_len = len(resposta_minima)
    return resposta_minima


print((subset(30, 40, [5, 5, 5, 5, 5, 10])))


                

