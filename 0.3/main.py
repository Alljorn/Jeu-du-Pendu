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
    for lettre, lettre_variantes in variantes.items():
        if c == lettre:
            caractere_to_check = list()
            for caractere in lettre_variantes:
                caractere_to_check.append(caractere)
            break

    for i in range( len(mot) ):
        for caractere in caractere_to_check:
            if caractere == mot[i]:
                etat = etat[:i] + caractere + etat[i+1:] 
    return etat


def mots_longueur ( liste_mots , n):
    """ fonction qui renvoie la liste des chaines d'une longueur donnée dans une liste
    préconditions :
    - liste_mots , de type liste de chaines de caractèe res
    - n, de type entier
    postconditions : liste de chaines de caractères : tous les éléments de mots qui ont la
    longueur n
    """
    word_list = list()
    for mot in liste_mots:
        if len(mot) == n:
            word_list.append(mot)
    return word_list


def mots_sans_lettre ( liste_mots , c):
    """ fonction qui renvoie la liste des ele ments d'une liste qui ne contiennent pas un
    caract ere donn e

    pre conditions :
    - liste_mots , de type liste de chaines de caract e res
    - c, de type caract ere

    postconditions : liste de chaine de caract e res
    """
    pass


def mots_avec_lettre ( liste_mots , c):
    """ fonction qui renvoie la liste des ele ments d'une liste qui
    contiennent un caract ere donn e

    pre conditions :
    - liste_mots , de type liste de chaines de caract e res
    - c, de type caract ere

    postconditions : liste de chaine de caract e res
    """
    c = c.upper()
    words_list = list()

    if variantes.get(c):
        for mot in liste_mots:
            for lettre in variantes[c]:
                if lettre in mot:
                    words_list.append(mot)
    else:
        for mot in liste_mots:
            if c in mot:
                words_list.append(mot)

    return words_list


def get_possible_word(liste_mots, impossible_letter, etat):
    etat_lettre_contenant = dict()
    for lettre in etat:
        if lettre != '-':
            if etat_lettre_contenant.get(lettre):
                etat_lettre_contenant[lettre] = etat_lettre_contenant[lettre] + 1
            else:
                etat_lettre_contenant[lettre] = 1
            for value in variantes.values():
                for i in range(len(value)):
                    if lettre == value[i]:
                        str_impossible_letter = value[:i] + value[i+1:] 
                        for letter_bis in str_impossible_letter:
                            if not letter_bis in impossible_letter:
                                impossible_letter.append(letter_bis)
    for key in etat_lettre_contenant.keys():
        if key in impossible_letter:
            impossible_letter.remove(key)
    words_possible = list()
    for mot in liste_mots:
        mot_lettre_contenant = dict()
        for lettre in mot:
            if mot_lettre_contenant.get(lettre):
                mot_lettre_contenant[lettre] = mot_lettre_contenant[lettre] + 1
            else:
                mot_lettre_contenant[lettre] = 1
        is_possible = True
        for lettre in mot:
            if lettre in impossible_letter:
                is_possible = False
                break
        if is_possible:
            for key, value in etat_lettre_contenant.items():
                if mot_lettre_contenant.get(key):
                    if mot_lettre_contenant[key] == value:
                        continue
                is_possible = False
                break
        if is_possible:
            for i in range(len(mot)):
                if etat[i] != '-':
                    if mot[i] != etat[i]:
                        is_possible = False
                        break
        if is_possible:
            words_possible.append(mot)
    return words_possible


def start_game(max_erreur = 8):
    path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+'/'+ "assets/littre.txt" # on récupère le chemin absolue où le scripte est executé, on rajoute le chemin du fichier littre.txt

    words = lire_mots(path)
    mot_secret = words[randint(0, len(words)-1)]   
    mot_secret = "EAU" 

    etat = "-" * len(mot_secret)

    nbr_erreur = 0

    lettre_entrer = list()
    lettre_fausse = list()

    # Recupération des mots possible pour la configuration de l'état
    liste_mots_possible = mots_longueur(words, len(mot_secret))
    
    while nbr_erreur < max_erreur and etat != mot_secret:
        print(f"Il y a encore {len(liste_mots_possible)} mot(s) possible(s)...")
        # Affichage de l'état
        print(etat)
        # Indication du nombre d'erreur
        print(f"Vous pouvez faire encore {max_erreur - nbr_erreur} erreur(s)")

        
        # Saisie de l'utilisateur
        caractere = input("Entrez une lettre , suivie d'un saut de ligne : ")
        if len(caractere) > 1 : # Vérification que la saisie est un caractère
            print("N'entrer qu'une lettre !")
            continue
        elif caractere in lettre_entrer: # Vérifie que le caratère n'a pas déjà été entré
            print("Cette lettre a déjà été entré !")
            continue
        lettre_entrer.append(caractere) # Ajout du caractère dans la liste des caractères déjà entrer

        
        # Redifinition de l'état avec le caractère saisie
        etat2 = nouvel_etat( mot_secret, etat, caractere)

        if etat2 == etat: # Si le caractère n'est pas présent dans le mot secret
            print("Dommage ...")
            lettre_fausse.append(caractere.upper())
            nbr_erreur += 1 # Ajout d'une erreur
        else: # Si il est présent
            print("Correct !")
            etat = etat2 # On redéfinie l'état à celui redéfinie avant

        liste_mots_possible = get_possible_word(liste_mots_possible, lettre_fausse, etat)


    print("-------------")
    if etat == mot_secret:
        print("Gagné ! Vous avez trouvé le mot secret ! ")
    else:
        print("Perdu !")

    print(f"Le mot secret était '{mot_secret}'")
    print("-------------")


start_game(8)

