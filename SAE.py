from ctypes.wintypes import HBITMAP
from random import randint

# Loto
choix = list(range(1,11))
shuffle(choix)
tirage = choix[0:n:1]
u = []
for i in range(n):
    c = int(input(f"Entrer le nombre {i+1} : "))
    while c < 1 or c > 10 or c in u:
        if c in u:
            print("Vous avez déjà choisi",c)
        else:
            print(c,"n'est pas compris entre 1 et 10")
        c = int(input(f"Entrer le nombre {i+1} : "))
    u.append(c)
gagnant = []
for c in n:
    if c in tirage:
        gagnant.append(c)
print("Vous avez choisi :",u)
print("Les nombres gagnants son :",tirage)
print(f"Vous avez {len(gagnant)} numéro gagnats : {gagnant}")








# Calcul du moyenne
somme = 0
nb = 0
note = float(input("Entrez une note entre 0 et 20 : "))
while note >=0 and note <=20:
    somme += note 
    nbNotes += 1
    note = float(input("Entrez une note entre 0 et 20"))
if nb == 0:
    print("Aucune note saisie")
else:
    print(f"{nb} notes saisies")
    print("Moyenne :",somme/nb)







hA = float(input("Entrez l'heure de départ du train A : "))*3600
vA = float(input("Entrez la vitesse en km/h du train A : ")/3.6
hB = float(input("Entrez l'heure de départ du train B : "))*3600
vB = float(input("Entrez la vitesse en km/h du train B : "))/3.6
t = hA 
if t > hB:
    t = hB
pA = 0
pB = float(input("Distance entre les trains A et B en km : "))*1000
while pA < pB:
    t +=1
    if t > hA:
        pA +=vA
    if t > hB:
        pB += vB
h = t//3600
m = (t//60)%60
s = t%60
print(f"Les trains A et B se rencontreront en {h} heures, {m} minutes et {s} secondes.")