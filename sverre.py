#Oppgave 1a)
print ('Oppgave 1a')
def multiplikasjonstabell(n):
    maks_produkt = n * n

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            resultat = a * b
            print(f"{resultat:4}", end="") 
        print()

multiplikasjonstabell(10)

print()

#Oppgave 1b)
print ('Oppgave 1b')
def multiplikasjonstabell(n):

    print(f"{' ':2} |", end="")  
    for a in range(1, n + 1):
        print(f"{a:4}", end="")  
    print() 

    print(f"{'-'*5}+{'-'*4*n}")

    for a in range(1, n + 1):
        print(f"{a:2} |", end="")  
        for b in range(1, n + 1):
            resultat = a * b
            print(f"{resultat:4}", end="")  
        print()  

multiplikasjonstabell(10)

print()

#Oppgave 2a)
print ('Oppgave 2a')
def fakultet_for_løkke(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        resultat = 1
        for a in range(1, n + 1):
            resultat *= a
        return resultat

print(fakultet_for_løkke(5))  

print()

#Oppgave 2b)
print ('Oppgave 2b')
def fakultet_while_løkke(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        resultat = 1
        a = 1
        while a <= n:
            resultat *= a
            a += 1
        return resultat

print(fakultet_while_løkke(6))



  