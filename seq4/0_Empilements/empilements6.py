from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)

nbCubesX = g.NB_CUBES_X


# votre code

def f0(g: CanevasEmpilements, pos: int) -> None:
    """empile un cube sur la position, si possible
    puis appelle pour empiler sur la position suivante"""

    # condition d'arrêt
    if pos < 0:
        return 

    # sinon
    g.empilerCube(pos, 'blue violet')  # empilement
    f0(g, pos - 1)  # appel récursif
    g.empilerCube(pos,'green')
    

f0(g, 9)


# fin du programme
g.attendreClic()
g.fermerFenetre()

