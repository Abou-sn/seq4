from libGrille import ouvrirFenetreGrille

# on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(50, 16, 12)

# on place des murs
for i, j in [
    (2, 0),
    (2, 1),
    (2, 2),
    (3, 3),
    (4, 3),
    (4, 4),
    (5, 4),
    (5, 5),
    (5, 6),
    (4, 7),
    (4, 8),
    (3, 9),
    (2, 8),
    (1, 7),
    (0, 7),
    (10, 6),
    (11, 7),
    (10, 8),
    (9, 7),
]:
    g.changerCarre(i, j, "black")

# démo déplacement

# on fait avancer pacman jusqu'à une case non valide
# et on garde sa trace en bleu

px, py = 9, 2  # position de pacman
dx, dy = 0, 1  # deplacement de pacman vers le bas

g.placer_pacman(px, py)
g.changerCarre(px, py, "blue")


Directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

nb_ckeck = 1
while True:
    for dx, dy in Directions: # on va chez les voisins
        vx, vy = px + dx, py + dy
        nb_ckeck += 1
        if g.case_valide(vx, vy) and g.getCouleur(vx, vy) != "blue":
            g.placer_pacman(vx, vy)
            g.dessinerFleche(px,py,vx,vy)
            g.changerCarre(vx, vy, "blue")
            g.pause(0.2)
            px, py = vx, vy
            nb_ckeck = 1
            break
        
    if nb_ckeck >= len(Directions): # aucun voisin dispo
        break


# fin du programme
g.attendreClic()
g.fermerFenetre()
