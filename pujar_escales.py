# et donen un nombre n que és el nombre d'escales que has de pujar, les pots pujar d'un en un o de dos en dos, 
# has de retornar totes les maneres d'arribar a n  

def countWays(n):
    prev = 1
    prev2 = 1
    # Running for loop to count all possible ways
    for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev
 
n = 200
print("Number of Ways : ", countWays(n))
        
