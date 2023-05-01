from pytokr import item
def canvi_minim_resposta_1604(e,c,monedes=[0.01,0.02,0.05,0.10,0.20,0.50,1,2], bitllets=[5,10,20,50,100,200,500]): 
    quantitat = e+(c/100)
    opcions = sorted(bitllets+monedes, reverse=True)
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

def generació_resposta(a,b): 
    llista_respostes = canvi_minim_resposta_1604(a,b)
    print('Bitllets de 500 euros:', comptar(500,llista_respostes))
    print('Bitllets de 200 euros:', comptar(200,llista_respostes))
    print('Bitllets de 100 euros:', comptar(100,llista_respostes))
    print('Bitllets de 50 euros:', comptar(50,llista_respostes))
    print('Bitllets de 20 euros:', comptar(20,llista_respostes))
    print('Bitllets de 10 euros:', comptar(10,llista_respostes))
    print('Bitllets de 5 euros:', comptar(5,llista_respostes))
    print('Monedes de 2 euros:', comptar(2,llista_respostes))
    print('Monedes de 1 euro:', comptar(1,llista_respostes))
    print('Monedes de 50 centims:', comptar(0.5,llista_respostes))
    print('Monedes de 20 centims:', comptar(0.2,llista_respostes))
    print('Monedes de 10 centims:', comptar(0.1,llista_respostes))
    print('Monedes de 5 centims:', comptar(0.05,llista_respostes))
    print('Monedes de 2 centims:', comptar(0.02,llista_respostes))
    print('Monedes de 1 centim:', comptar(0.01,llista_respostes))

    
def comptar(n,llista): 
    count = 0 
    for i in llista: 
        if i == n: 
            count += 1
    return count

#generació_resposta(9999,99)
e = int(item())
c = int(item())
generació_resposta(e,c)

