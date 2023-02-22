import random
#import time

def czyWygrana():
    x = 0
    global zajęte
    if(gora[0] == gora [1] == gora [2]):
        wypiszTablice()
        print("Koniec " + gora[0] + " wygrał!")
        return False
    elif(srodek[0] == srodek [1] == srodek [2]):
        wypiszTablice()
        print("Koniec " + srodek[0] + " wygrał!")
        return False
    elif(dol[0] == dol [1] == dol [2]):
        wypiszTablice()
        print("Koniec " + dol[0] + " wygrał!")
        return False
    elif((gora[x] == srodek[x+1] == dol[x+2]) or (gora[x+2] == srodek[x+1] == dol[x])):
        wypiszTablice()
        print("Koniec " + srodek[x+1] + " wygrał!")
        return False
    elif(len(zajęte) == 9):
        wypiszTablice()
        print("Nikt nie wygrał, remis")
        return False
    else:
        for x in range(3):
            if(gora[x] == srodek[x] == dol[x]):
                wypiszTablice()
                print("Koniec " + srodek[x] + " wygrał!")
                return False    
    return True
      
def wstaw(liczba, znak):
    if(liczba == 1):
        gora[0] = "[" + znak + "]"
    elif(liczba == 2):
        gora[1] = "[" + znak + "]"
    elif(liczba == 3):
        gora[2] = "[" + znak + "]"
    elif(liczba == 4):
        srodek[0] = "[" + znak + "]"
    elif(liczba == 5):
        srodek[1] = "[" + znak + "]"
    elif(liczba == 6):
        srodek[2] = "[" + znak + "]"
    elif(liczba == 7):
        dol[0] = "[" + znak + "]"
    elif(liczba == 8):
        dol[1] = "[" + znak + "]"
    elif(liczba == 9):
        dol[2] = "[" + znak + "]"

def wypiszTablice():
    print()
    for x in gora:
        print(x, end = " ")
    print()
    for x in srodek:
        print(x, end = " ")
    print()
    for x in dol:
        print(x, end = " ")


gora = ["[1]", "[2]", "[3]"]
srodek = ["[4]", "[5]", "[6]"]
dol = ["[7]", "[8]", "[9]"]
zajęte = []
możliwePola = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
ostatni = "O"

while(czyWygrana()):
    wypiszTablice()

    if(ostatni == "O"):
        while(True):
            X = int(input("\nCyfra do podstawienia X: "))
            if(str(X) in zajęte):
                print("Podane pole jest już zajęte, spróbuj jeszcze raz")
                continue
            wstaw(X, "X")
            ostatni = "X"
            zajęte += str(X)
            break
        continue
    #elif(ostatni == "X"): wersja dla dwóch graczy
    #    wstaw(int(input("\nCyfra do podstawienia O: ")), "O")
    #    ostatni = "O"
    #    continue
    #
    # wersja z PC->
    elif(ostatni == "X"):
        while(True):
            O = int(random.choice(możliwePola))
            if(str(O) in zajęte):
                continue
            #time.sleep(2)
            print("\nPole wybrane przez PC to:", O)
            wstaw(O, "O")
            ostatni = "O"
            zajęte += str(O)
            break
        print()
        continue

