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
    for res in llista_respostes[::-1]: 
        if res != '{}': 
            string = "{" + " ".join(str(i) for i in res) + "}"
            print(string)
        else: 
            print('{}')

#sumes_iguals_1904(6,7,[1,-2,0,3,-4,5,1])

def input(): 
    suma = int(item())
    n = int(item())
    llista = list()
    for _ in range(n): 
        llista.append(int(item()))
    return suma, n, llista 

suma,n,llista = input()
sumes_iguals_1904(suma,n,llista)









