
def subset_sum(input, total):
    T = [[False for _ in range(total + 1)] for _ in range(len(input) + 1)]
    for i in range(len(input) + 1):
        T[i][0] = True

    for i in range(1, len(input) + 1):
        for j in range(1, total + 1):
            if j - input[i - 1] >= 0:
                T[i][j] = T[i - 1][j] or T[i - 1][j - input[i - 1]]
            else:
                T[i][j] = T[i - 1][j]
    for i in T: 
        print(i)
    valor_final =T[len(input)][total]
    if valor_final == True: 
        # buscar quin són els elements que ho fan possible 
        def aux(fila = (len(input)), columna = total-1, resultat = []): 
            if columna == 0 or fila == 0: #hem arribat al principi de la taula 
                return resultat
            elif T[fila-1][columna] == True: # no afegim res
                return aux(fila-1,columna,resultat)
            else: # el true no ve del true de dalt 
                resultat.append(input[fila-1])
                return aux(fila-1,columna-input[fila-1],resultat[:])
        
        return aux()
        
    else: 
        return []    

print(subset_sum([60, 15, 25, 95, 80, 5, 10, 5, 10, 75],100))
    

