def est_sous_chaine(s1,s2):
    if s1 == "" :
        return True
    if s2 == "" :
        return False
    if s1[0]== s2[0] :
        return est_sous_chaine(s1[1:], s2[1:])
    else :
        return est_sous_chaine(s1, s2[1:])
    

s1 = 'Abou'
s2 = 'Aboubacar SECK'

print(est_sous_chaine(s1,s2))

t1 = 'ASECK'

print(est_sous_chaine(t1,s2))