def n_queens(n): 
    columns = set() # ens servirà per saber quines columnes estan ocupades
    posDiags = set() # ens servirà per saber les diagonals positives ocupades 
        # sabem que serà un constant de row + column 
    negDiags = set() # diagonals neg ocupades 
        # sabem que serà un constant de row - column 

    res = 0 
    respostes_finals = []
    def backtrack(row,respostes = []): 
        nonlocal res, respostes_finals
        if row == n: # estem al final, hem trobat un tauler vàlid 
            res += 1
            respostes_finals.append(respostes[:])        
            return 
        #n^n
        for column in range(n): 
            if column in columns or (row+column) in posDiags or (row-column) in negDiags: 
                continue 
            respostes.append((row,column))
            columns.add(column)  
            posDiags.add(row+column)
            negDiags.add(row-column)
            backtrack(row+1)
            columns.remove(column)
            posDiags.remove(row+column)
            negDiags.remove(row-column)
            respostes.pop()
        
    backtrack(0)
    return res, respostes_finals

res,respostes_finals = n_queens(4)
print("Nombre total de solucions:", res)

for i in range(res):
    print("Solució", i+1, ":", respostes_finals[i])




