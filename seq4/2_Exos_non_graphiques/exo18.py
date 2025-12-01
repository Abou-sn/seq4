def somme(n):
    if n == 0 :
        return 0
    else :
        return n**2+somme((n-1))

print(somme(3))