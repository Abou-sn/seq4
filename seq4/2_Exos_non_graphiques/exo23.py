arborescence = [[['a',['b','c',['d'],'e',['f','g']],
['h',['i',['j','k']]],['l','m']]],['n','o','p'],['q','r'],
[[['s'],[['t','u']],'v'],'w','x',[['y'],'z']]]

def compte_str(arb) :
    if isinstance(arb,str) :
        return 1
    else :
        S = 0
        for e in arb: 
            S += compte_str(e)
        return S
        
def afficher_str (arb): 
    if isinstance(arb,str) :
        print(arb, end=' ')
    else :
        for e in arb: 
            afficher_str(e)
        

def compression(tab):
    l = []
    cpt = 0
    nbCourant = tab[0]
    for i in range (len(tab)):
        if nbCourant == tab[i]:
            cpt+=1
        else :
            l.append(cpt)
            l.append(nbCourant)
            cpt = 0
            nbCourant = tab[i]

    return l

tab = [5,5,5,5,5,5,5]

def cpt_points(s,i):
    if i >= len(s):
        return 0
    elif s[i] == '.':
        return 1 + cpt_points(s,i+1)
    
print(cpt_points("...",0))
