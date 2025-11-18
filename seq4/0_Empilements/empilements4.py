from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)

# on recupere le nb de cubes maximal sur une ligne
# (en principe c'est 10 si vous ne changez pas les paramètres)
nbCubesX = g.NB_CUBES_X


# on définit deux fonctions
def f0(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos, "blue")
    g.attendreClic()

    if pos + 1 < nbCubesX:
        f1(g, pos + 1)


def f1(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos, "yellow")
    g.attendreClic()

    if pos + 1 < nbCubesX:
        f0(g, pos + 1)


# fin du programme
g.attendreClic()
g.fermerFenetre()
