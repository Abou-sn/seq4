def est_sous_chaine(s1,s2):
    if s1 == "" :
        return True
    if s2 == "" :
        return False
    if s1[0] == s2[0] :
        return est_sous_chaine(s1[1:], s2[1:])
    else :
        return est_sous_chaine(s1, s2[1:])
    
def prefixe_commun(s1,s2):
    if s1 == "" or s2 =="" :
        return ""
    if s1[0] != s2[0] :
        return ""
    if s1 == s2 :
        return s1
    if s1[0] == s2[0] :
        return s1[0] + prefixe_commun(s1[1:],s2[1:])
    
assert prefixe_commun("guitare", "guimauve") == "gui"
assert prefixe_commun("cartes", "carbone") == "car"
assert prefixe_commun("python", "java") == ""
assert prefixe_commun("test", "test") == "test"
