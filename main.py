#!/usr/bin/env python3
def somma (a,b):
    return a+b

def sottrazione (a,b):
    return a-b

def moltiplicazione (a,b):
    return a*b

def divisione (a,b):
    return a/b

msg = """
    scegli l'operazione da fare
   0 esci
   1 somma 
   2 sottrazione
   3 moltiplicazione
   4 divisione
    """
while True:
    print(msg)

    s = input("scegli: ")
    if s == "1":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("il risultato e': ", somma(a,b))

    elif s == "2":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("il risultato e': ", sottrazione(a,b))

    elif s == "3":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("il risultato e': ", moltiplicazione(a,b))

    elif s == "4":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("il risultato e': ", divisione(a,b))

    elif s == "0":
        break