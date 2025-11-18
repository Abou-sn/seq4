from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)


# on définit trois fonctions
def f0(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos, "green")
    g.attendreClic()
    f1(g, pos + 1)


def f1(g: CanevasEmpilements, pos: int) -> None:
    f2(g, pos - 1)
    g.attendreClic()
    g.empilerCube(pos, "yellow")
    g.attendreClic()
    f2(g, pos + 1)


def f2(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos + 2, "blue")


# on lance la fonction f1
f0(g, 2)


# fin du programme
g.attendreClic()
g.fermerFenetre()
