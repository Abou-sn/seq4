import tkinter as tk

import tkiteasy as tke


class CanevasEmpilements(tke.Canevas):
    """
    Etend le Canevas de tkiteasy en ajoutant l'empilement de cube
    """

    def __init__(self, parent: tk.Misc, largeur: float, hauteur: float):
        """
        w : largeur en pixels
        h : hauteur en pixels"""
        super().__init__(parent, largeur, hauteur)

        self.LARGEUR = largeur
        self.HAUTEUR = hauteur
        self.COTE_CUBES = 80
        self.NB_CUBES_X = int(self.LARGEUR / self.COTE_CUBES)
        self.NB_CUBES_Y = int(self.HAUTEUR / self.COTE_CUBES) - 1
        self.tab_cubes: list[list[tke._Color]] = [[] for _ in range(self.NB_CUBES_X)]

        self.dessinerLigne(
            0,
            self.HAUTEUR - self.COTE_CUBES + 2,
            self.LARGEUR,
            self.HAUTEUR - self.COTE_CUBES + 2,
            "white",
        )
        for i in range(self.NB_CUBES_X):
            self.afficherTexte(
                str(i),
                int(self.COTE_CUBES * (0.5 + i)),
                int(self.HAUTEUR - self.COTE_CUBES / 2),
                "white",
                20,
            )

    def empilerCube(self, pos: int, couleur: tke._Color) -> None:
        if 0 <= pos < self.NB_CUBES_X and len(self.tab_cubes[pos]) < self.NB_CUBES_Y:
            self.tab_cubes[pos].append(couleur)
            c = self.dessinerRectangle(
                pos * self.COTE_CUBES + 1,
                0,
                self.COTE_CUBES - 1,
                self.COTE_CUBES - 1,
                couleur,
            )
            self.actualiser()
            self.pause(0.2)

            step = 5
            yfinal = self.HAUTEUR - (1 + len(self.tab_cubes[pos])) * self.COTE_CUBES
            while c.y < yfinal:
                self.deplacer(c, 0, step)
                self.pause(0.0003 * step)
                self.actualiser()


def ouvrirFenetreEmpilements(
    largeur: float = 800, hauteur: float = 600
) -> CanevasEmpilements:
    return CanevasEmpilements(tk.Tk(), largeur, hauteur)
