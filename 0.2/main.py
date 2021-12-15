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


variantes = {
    'A' : f'A{chr(192)}{chr(196)}{chr(194)}{chr(198)}',
    'C' : f'C{chr(199)}',
    'E' : f'E{chr(202)}{chr(200)}{chr(201)}{chr(203)}{chr(198)}{chr(338)}',
    'I' : f'I{chr(206)}{chr(207)}',
    'O' : f'O{chr(212)}{chr(214)}{chr(338)}',
    'U' : f'U{chr(217)}{chr(220)}{chr(219)}'
}
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

    caractere_to_check = [c]
    for lettre, lettre_variantes  in variantes.items():
        if c == lettre:
            caractere_to_check = list()
            for caractere in lettre_variantes:
                caractere_to_check.append(caractere)
            break

    for i in range( len(mot) ):
        for caractere in caractere_to_check:
            if caractere == mot[i]:
                etat = etat[:i] + caractere + etat[i+1:]
                break
    return etat


def start_game(max_erreur = 8):
    path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+'/'+ "assets/littre.txt" # on récupère le chemin absolue où le scripte est executé, on rajoute le chemin du fichier littre.txt

    words = lire_mots(path)
    mot = words[randint(0, len(words)-1)]
    print(mot)

    etat = "-" * len(mot)

    nbr_erreur = 0

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


start_game(8)

