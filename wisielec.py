licznik = 0
def sprawdz(litera):
    if(litera in podaneLiterki):
        print("litera została już podana")
    elif len(literka) > 1:
        print("podaj literkę a nie słowo")
    elif(litera in hasło):
        i = 0
        for znak in hasło:
            if(znak == litera):
                ukryteHasło[i] = litera
            i += 1
    else:
        global licznik
        licznik += 1
        
    if(litera not in podaneLiterki):
        podaneLiterki.append(litera)


def wygrana():
    i = 0
    global licznik 
    if(licznik == 10):
        return False
    for znak in hasło:
        if(znak != ukryteHasło[i]):
            return True
        else:
            i+=1
    return False

hasło = input("Podaj hasło: ")
kategoria = input("Podaj kategorię hasła: ")
ukryteHasło = []
podaneLiterki = []
for znak in hasło:
    if(znak == " "):
        ukryteHasło.append(" ")
    else:
        ukryteHasło.append("_")

while(wygrana()):
    print("\n\nKategoria: " + kategoria + "\n")
    for znak in ukryteHasło:
        print(znak, end = '')
    print("\nLiterki które zostały już wykorzystane: ")
    for literka in podaneLiterki:
        print(literka, end =' ')
    print("\nbłędy: " + str(licznik) + "/10")
    sprawdz(input("Podaj literę: "))

print("\n\nKategoria: " + kategoria + "\n")
for znak in ukryteHasło:
    print(znak, end = '')
print("\nLiterki które zostały już wykorzystane: ")
for literka in podaneLiterki:
    print(literka, end =' ')
print("\nbłędy: " + str(licznik) + "/10\n")
if licznik == 10:
    print("Porażka, hasło to: " + hasło)
else:
    print("Wygrana, hasło to: " + hasło)
    
