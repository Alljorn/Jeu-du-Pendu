import os

from tkinter import *
from random import randint


class Pendu_Game:

    variantes = {
            'A' : f'A{chr(192)}{chr(196)}{chr(194)}{chr(198)}',
            'C' : f'C{chr(199)}',
            'E' : f'E{chr(202)}{chr(200)}{chr(201)}{chr(203)}{chr(198)}{chr(338)}',
            'I' : f'I{chr(206)}{chr(207)}',
            'O' : f'O{chr(212)}{chr(214)}{chr(338)}',
            'U' : f'U{chr(217)}{chr(220)}{chr(219)}'
    }

    def __init__(self, bg='#FFFFFF'):
        self.color_bg = bg
        self.path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        
        self.list_words = Pendu_Game.lire_mots(self.path+"/assets/littre.txt")
        self.mot_secret = self.list_words[randint(0, len(self.list_words)-1)]
        self.etat = "-" * len(self.mot_secret)
        self.nbr_erreur = 0
        self.max_erreur = 6
        self.lettre_entre = list()
        self.lettre_fausse = list()
        self.liste_mots_possible = Pendu_Game.mots_longueur(self.list_words, len(self.mot_secret))


    def run(self):
        self.window = Tk()

        self.pendu_images = [PhotoImage(file=self.path+f"/assets/{i}.png").subsample(2) for i in range(1, 9)]

        self.window.title("Pendu !") # Titre de la fenêtre
        self.window.iconbitmap(self.path+"/assets/icon.ico") # Icône de la fenêtre
        self.window.config(background="#FFFFFF") # Arrière plan

        # Taille et position de la fenêtre
        width, height = 720, 480 # Taille de la fenêtre
        left_pos = (self.window.winfo_screenwidth() - width) / 2 # Position par raport à la gauche de l'écran
        top_pos = (self.window.winfo_screenheight() - height) / 4 # Position par raport à la droite de l'écran
        self.window.geometry( "%dx%d+%d+%d" % (width, height, left_pos, top_pos)) # Application de la taille et de la position
        self.window.resizable(0,0)

        # Création d'une barre de menu
        menu_bar = Menu(self.window)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nouveau")
        file_menu.add_command(label="Quitter", command=self.window.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Selctionner tout")
        edit_menu.add_command(label="Annuler")
        menu_bar.add_cascade(label="Edition", menu=edit_menu)

        self.window.config(menu=menu_bar)


        self.frame_top = Frame(self.window, bg=self.color_bg)
        self.title = Label(self.frame_top, text="Pendu !", font=("Courrier", 25), bg=self.color_bg)

        self.espace = Frame(self.window, bg=self.color_bg)

        self.frame_middle = Frame(self.window, bg=self.color_bg)
        self.label_etat = Label(self.frame_middle, text=self.etat, font=("Courrier"), bg=self.color_bg)
        self.label_info_nbr_mot = Label(self.frame_middle, text=f"Nombre de mot possible: {len(self.liste_mots_possible)}", bg=self.color_bg, width=25)
        self.entry_letter = Entry(self.frame_middle, bg=self.color_bg)
        self.entry_boutton = Button(self.frame_middle, text="Entrer", font=("Courrier"), bg=self.color_bg, command=self.update)

        self.console_frame = Frame(self.window, bg=self.color_bg)
        self.label_console = Label(self.console_frame, width=720, bg=self.color_bg)

        self.frame_buttom = Frame(self.window, bg=self.color_bg)
        self.label_image = Label(self.frame_buttom, width=150, height=150 , bg=self.color_bg, image=self.pendu_images[self.nbr_erreur])
        self.frame_info_lettre = Frame(self.frame_buttom, bg=self.color_bg)
        self.label_info_lettres = Label(self.frame_info_lettre, text="Lettre possible:", font=("Courrier", 20), bg=self.color_bg)
        self.label_lettres = Label(self.frame_info_lettre, text=self.get_possible_letter(), font=("Courrier", 10), bg=self.color_bg)

        
        self.title.pack(expand=YES, fill=X)
        self.frame_top.pack(fill=X)

        
        self.espace.pack(expand=YES, fill=X)


        self.label_etat.grid(row=0, column=1)
        self.label_info_nbr_mot.grid(row=1, column=0)
        self.entry_letter.grid(row=1, column=1, padx=125)
        self.entry_boutton.grid(row=1, column=2)
        self.frame_middle.pack(expand=YES, fill=X)


        self.label_console.pack(fill=Y)
        self.console_frame.pack(expand=YES, fill=Y)


        self.label_image.grid(row=0, column=0)
        self.frame_info_lettre.grid(row=0, column=1)
        self.label_info_lettres.pack(padx=150)
        self.label_lettres.pack()
        self.frame_buttom.pack(expand=YES, fill=X)

        
        self.window.mainloop()

    def get_possible_letter(self):
        possible_letter = ""
        for i in range(26):
            if not (chr(65+i) in self.lettre_fausse or chr(97+i) in self.lettre_entre):
                possible_letter += chr(65+i).lower() + " "
        return possible_letter


    @staticmethod
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


    @staticmethod
    def mots_longueur (liste_mots , n):
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


    @staticmethod
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
        for lettre, lettre_variantes in Pendu_Game.variantes.items():
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


    @staticmethod
    def get_possible_word(liste_mots, impossible_letter, etat):
        etat_lettre_contenant = dict()
        for lettre in etat:
            if lettre != '-':
                if etat_lettre_contenant.get(lettre): etat_lettre_contenant[lettre] = etat_lettre_contenant[lettre] + 1
                else: etat_lettre_contenant[lettre] = 1
                for value in Pendu_Game.variantes.values():
                    for i in range(len(value)):
                        if lettre == value[i]:
                            str_impossible_letter = value[:i] + value[i+1:] 
                            for letter_bis in str_impossible_letter:
                                if not letter_bis in impossible_letter:
                                    impossible_letter.append(letter_bis)
        for key in etat_lettre_contenant.keys():
            if key in impossible_letter: impossible_letter.remove(key)
        words_possible = list()
        for mot in liste_mots:
            mot_lettre_contenant = dict()
            for lettre in mot:
                if mot_lettre_contenant.get(lettre): mot_lettre_contenant[lettre] = mot_lettre_contenant[lettre] + 1
                else:  mot_lettre_contenant[lettre] = 1
            is_possible = True
            for lettre in mot:
                if lettre in impossible_letter:
                    is_possible = False
                    break
            if is_possible:
                for key, value in etat_lettre_contenant.items():
                    if mot_lettre_contenant.get(key):
                        if mot_lettre_contenant[key] == value: continue
                    is_possible = False
                    break
            if is_possible:
                for i in range(len(mot)):
                    if etat[i] != '-':
                        if mot[i] != etat[i]:
                            is_possible = False
                            break
            if is_possible: words_possible.append(mot)
        return words_possible

    
    def print_label_console(self, _text):
        self.label_console.config(text=_text)


    def update_widget(self):
        self.label_info_nbr_mot.config(text=f"Nombre de mot possible: {len(self.liste_mots_possible)}")
        self.label_etat.config(text=self.etat)
        self.label_lettres.config(text=self.get_possible_letter())
        self.label_image.config(image=self.pendu_images[self.nbr_erreur])
        self.entry_letter.delete(0, 'end')


    def update(self):
        if self.nbr_erreur < self.max_erreur and self.etat != self.mot_secret:
            print(f"Il y a encore {len(self.liste_mots_possible)} mot(s) possible(s)...")
            # Affichage de l'état
            print(self.etat)
            # Indication du nombre d'erreur
            print(f"Vous pouvez faire encore {self.max_erreur - self.nbr_erreur} erreur(s)")

            
            # Saisie de l'utilisateur
            caractere = self.entry_letter.get()
            # if len(caractere) > 1 : # Vérification que la saisie est un caractère
            #     print("N'entrer qu'une lettre !")
            #     continue
            # elif caractere in self.lettre_entrer: # Vérifie que le caratère n'a pas déjà été entré
            #     print("Cette lettre a déjà été entré !")
            #     continue
            self.lettre_entre.append(caractere) # Ajout du caractère dans la liste des caractères déjà entrer

            
            # Redifinition de l'état avec le caractère saisie
            etat2 = Pendu_Game.nouvel_etat( self.mot_secret, self.etat, caractere)

            if etat2 == self.etat: # Si le caractère n'est pas présent dans le mot secret
                self.print_label_console("Dommage ...")
                self.lettre_fausse.append(caractere.upper())
                self.nbr_erreur += 1 # Ajout d'une erreur
            else: # Si il est présent
                self.print_label_console("Correct !")
                self.etat = etat2 # On redéfinie l'état à celui redéfinie avant
            self.liste_mots_possible = Pendu_Game.get_possible_word(self.liste_mots_possible, self.lettre_fausse, self.etat)

            self.update_widget()


        
        else:
            print("-------------")
            if self.etat == self.mot_secret:
                print("Gagné ! Vous avez trouvé le mot secret ! ")
            else:
                self.nbr_erreur += 1 # Ajout d'une erreur
                self.update_widget()
                self.print_label_console("Perdu !\n :(")
                print("Perdu !")

            print(f"Le mot secret était '{self.mot_secret}'")
            print("-------------")
            


game = Pendu_Game(bg='#F9F9F9')
game.run()
