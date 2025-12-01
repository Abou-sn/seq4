def puissance(n, k):
    # Cas de base : n puissance 0 vaut toujours 1
    if k == 0:
        return 1
    # Appel récursif : n * (n puissance k-1)
    else:
        return n * puissance(n, k - 1)

# Test (n'oublie pas le print pour voir le résultat !)
print(puissance(2, 3))  # Doit afficher 8