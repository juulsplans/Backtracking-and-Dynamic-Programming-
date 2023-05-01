
def combination_sum_90(candidats, target): 
    candidats.sort() # ens ajudarà amb els replicats 
    res = []
    def backtrack(cur,pos,target): 
        if target == 0: 
            res.append(cur.copy())
        elif target <= 0: 
            return 
        
        prev = -1
        for i in range(pos,len(candidats)): 
            if candidats[i] == prev: 
                continue 
            cur.append(candidats[i])
            backtrack(cur,i+1,target-candidats[i])
            cur.pop()
            prev = candidats[i]
        backtrack([],0,target)

        return res

