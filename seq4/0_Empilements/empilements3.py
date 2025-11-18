from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)


# on définit trois fonctions
def fA(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos, "white")
    g.attendreClic()
    fB(g, pos - 1)
    g.empilerCube(pos + 1, "green")
    g.attendreClic()
    fB(g, pos + 1)
    g.empilerCube(pos + 2, "blue")
    g.attendreClic()


def fB(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos, "yellow")
    g.empilerCube(pos + 1, "yellow")
    g.attendreClic()


# fin du programme
g.attendreClic()
g.fermerFenetre()
