def tous_positifs(t : list[int], debut : int ) -> bool :
    if len(t) == debut :
        return True
    
    if t[debut]<=0 :
        return False
    else :
        return tous_positifs(t,debut+1)
    

tplus = [i for i in range (1,10)]
tmoins =[-i for i in range(10)]
tmix = [1,6,1,6,-5,-546,14]
tmix2 = [-12,5,5,2,6]

assert tous_positifs(tplus,0) == True
assert tous_positifs(tmoins,0) == False
assert tous_positifs(tmix,0) == False
assert tous_positifs(tmix2,1) == True

