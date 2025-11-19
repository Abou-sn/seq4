from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)

nbCubesX = g.NB_CUBES_X
nbCubesY = g.NB_CUBES_Y


# votre code
def f1(g: CanevasEmpilements, pos: int, pil: int):
    if pil >= nbCubesY :
        return
    f0(g,pos)
    f1(g,pos,pil+1)


def f0(g: CanevasEmpilements, pos: int) -> None:
    """empile un cube sur la position, si possible
    puis appelle pour empiler sur la position suivante"""

    # condition d'arrêt
    if pos >= nbCubesX :
        return 

    # sinon
    g.empilerCube(pos, 'blue violet')  # empilement
    f0(g, pos + 1)  # appel récursif
    g.empilerCube(pos,'green')
# fin du programme

f1(g,0,0)
g.attendreClic()
g.fermerFenetre()
