from random import randint
import os

def lire_mots ( nom_fichier):
    """ fonction qui récupère la liste des mots dans un fichier

    préconditions
    - nom_fichier , de type chaine de caractère : nom du fichier contenant les mots
    (un par ligne )

    postconditions : liste de chaine de caractères
    """
    liste_mots = [] # le tableau qui contiendra les lignes
    f = open ( nom_fichier , encoding ="UTF -8") # on ouvre le fichier
    ligne = f. readline () # une variable temporaire pour récupérer la ligne courante dans le fichier f
    while ligne != "":
        liste_mots . append ( ligne . strip () ) # on rajoute la ligne courante dans le tableau
        ligne = f. readline () # on récupère la ligne suivante
    return liste_mots


def nouvel_etat ( mot , etat , c) :
    """ fonction qui renvoie le nouvel état après proposition d’une lettre c

    préconditions :
    - mot , de type chaine de caractères ,
    - etat , de type chaine de caractères : les lettres inconnues sont
    représentées par des ’_ ’. Cette chaine a la mËme longueur que le paramètre mot ,
    - c, de type caractère : la lettre proposée.

    postconditions : chaine de caractère o`u les "_" correspondant au paramètre c ont été remplac és
    par c
    """
    c = c.upper()
    for i in range( len(mot) ):
        if c == mot[i]:
            etat = etat[:i] + c + etat[i+1:]
    return etat


path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+'/'+ "assets/littre.txt" # on récupère le chemin absolue où le scripte est executé, on rajoute le chemin du fichier littre.txt

words = lire_mots(path)
mot = words[randint(0, len(words)-1)]
print(mot)

etat = "-" * len(mot)

nbr_erreur = 0
max_erreur = 8

while nbr_erreur < max_erreur and etat != mot:
    print(etat)
    print(f"Vous pouvez faire encore {max_erreur - nbr_erreur} erreur(s)")
    caractere = input("Entrez une lettre , suivie d'un saut de ligne : ")
    etat2 = nouvel_etat( mot, etat, caractere)
    if etat2 == etat:
        print("Dommage ...")
        nbr_erreur += 1
    else:
        print("Bravo !")
    etat = etat2

print()
if etat == mot:
    print("Gagné !")
else:
    print("Perdu !")

print(f"Le mot secret était '{mot}'")


