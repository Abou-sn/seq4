from libEmpilements import CanevasEmpilements, ouvrirFenetreEmpilements

g = ouvrirFenetreEmpilements(800, 600)


# on définit trois fonctions
def fa(g: CanevasEmpilements, pos: int) -> None:
    fb(g, pos + 1)
    g.empilerCube(pos, "green")
    g.attendreClic()
    fb(g, pos)


def fb(g: CanevasEmpilements, pos: int) -> None:
    fc(g, pos)
    g.attendreClic()
    g.empilerCube(pos, "yellow")


def fc(g: CanevasEmpilements, pos: int) -> None:
    g.empilerCube(pos + 2, "blue")
    g.attendreClic()

fa(g,2)
# fin du programme
g.attendreClic()
g.fermerFenetre()

