def sumes_iguals(s, n, llista):
    def backtrack(i=0, llista_res=[], llista_curr=set(), suma=s):
        if suma == 0 and i!= 0: 
            llista_res.append(llista_curr)  
            return 
        elif suma == 0 and i == 0: 
            llista_res.append('{}')
        while i < n and llista[i] <= suma: 
            llista_curr.add(llista[i])
            backtrack(i+1, llista_res, set(llista_curr), suma-llista[i])
            llista_curr.remove(llista[i])
            i += 1
        return
    llista_results = []
    backtrack(0, llista_results, set(), s)
    
    for i in llista_results: 
        print(i)

sumes_iguals(6,7,[1,6,0,1,3,0,2])

