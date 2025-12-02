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
        
print(compte_str(arborescence))
