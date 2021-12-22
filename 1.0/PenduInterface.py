import os

from tkinter import *
from random import randint


class Pendu_Game:

    # Dictionnaire de variante des lettres A, C, E, I, O, U
    variantes = {
            'A' : f'A{chr(192)}{chr(196)}{chr(194)}{chr(198)}',
            'C' : f'C{chr(199)}',
            'E' : f'E{chr(202)}{chr(200)}{chr(201)}{chr(203)}{chr(198)}{chr(338)}',
            'I' : f'I{chr(206)}{chr(207)}',
            'O' : f'O{chr(212)}{chr(214)}{chr(338)}',
            'U' : f'U{chr(217)}{chr(220)}{chr(219)}'
    }


    def __init__(self, bg='#FFFFFF'):
        self.color_bg = bg # Couleur du fond d'écran
        self.path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') # Chemin d'accès au fichier executer
        
        self.list_words = Pendu_Game.lire_mots(self.path+"/assets/littre.txt") # Liste des mots présent dans le fichier 'littre.txt'
        # Initialise toute les variables nécessaire au programme
        self.mot_secret = str()
        self.etat = str()
        self.nbr_erreur = int()
        self.max_erreur = int()
        self.lettre_entre = list()
        self.lettre_fausse = list()
        self.liste_mots_possible = list()

        self.is_init = False
        self.help_window = None
        self.is_help_window_creat = False

        # Création de la fenêtre
        self.window = Tk()
        
        # Chargement des images 1.png, 2.png, 3.png, 4.png, 5.png, 6.png, 7.png et 8.png
        self.pendu_images = [PhotoImage(file=self.path+f"/assets/{i}.png").subsample(2) for i in range(1, 9)]

        # Personnalisation de la fenêtre
        self.window.title("Pendu !") # Titre de la fenêtre
        self.window.iconbitmap(self.path+"/assets/icon.ico") # Icône de la fenêtre
        self.window.config(background=self.color_bg) # Arrière plan

        # Taille et position de la fenêtre
        width, height = 720, 480 # Taille de la fenêtre
        left_pos = (self.window.winfo_screenwidth() - width) / 2 # Position par raport à la gauche de l'écran
        top_pos = (self.window.winfo_screenheight() - height) / 4 # Position par raport à la droite de l'écran
        self.window.geometry( "%dx%d+%d+%d" % (width, height, left_pos, top_pos)) # Application de la taille et de la position
        self.window.resizable(0,0) # Désactive la redimention

        # Création d'une barre de menu
        menu_bar = Menu(self.window)

        # Ajout de la cascade 'Jeu' et de ses commandes
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nouveau", command=self.init_game)
        file_menu.add_command(label="Quitter", command=self.window.quit)
        menu_bar.add_cascade(label="Jeu", menu=file_menu)

        # Ajout de la cascade 'Aide' et de sa commande
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Comment jouer ?", command=self.creat_help_window)
        menu_bar.add_cascade(label="Aide", menu=edit_menu)

        self.window.config(menu=menu_bar)

        # Création de l'interface
        self.frame_top = Frame(self.window, bg=self.color_bg)
        self.title = Label(self.frame_top, text="Pendu !", font=("Courrier", 25), bg=self.color_bg) # Titre 'Pendu !'

        self.espace = Frame(self.window, bg=self.color_bg)

        self.frame_middle = Frame(self.window, bg=self.color_bg)
        self.label_etat = Label(self.frame_middle, text=self.etat, font=("Courrier"), bg=self.color_bg) # L'état du mot
        self.label_info_nbr_mot = Label(self.frame_middle, text=f"Nombre de mot possible: {len(self.liste_mots_possible)}", bg=self.color_bg, width=24) # Information du nombre de mot possible
        self.entry_letter = Entry(self.frame_middle, bg=self.color_bg) # La boite de saisie
        self.entry_boutton = Button(self.frame_middle, text="Entrer", font=("Courrier"), bg=self.color_bg, command=self.update) # Le bouton 'entrer'

        self.console_frame = Frame(self.window, bg=self.color_bg)
        self.label_console = Label(self.console_frame, width=720, bg=self.color_bg) # Label de dialogue

        self.frame_buttom = Frame(self.window, bg=self.color_bg)
        self.label_image = Label(self.frame_buttom, width=150, height=150 , bg=self.color_bg, image=self.pendu_images[self.nbr_erreur]) # L'affichage des images
        self.frame_info_lettre = Frame(self.frame_buttom, bg=self.color_bg)
        self.label_info_lettres = Label(self.frame_info_lettre, text="Lettre possible:", font=("Courrier", 20), bg=self.color_bg)
        self.label_lettres = Label(self.frame_info_lettre, text=self.get_possible_letter(), font=("Courrier", 10), bg=self.color_bg) # Les lettre restate

        
        # Placement des widjets
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

        # Initialisation d'une nouvelle partie
        self.init_game()
        

    def init_game(self):
        # Fontion d'initialisation d'une partie
        self.mot_secret = self.list_words[randint(0, len(self.list_words)-1)] # Chosie un mot aléatoire dans la liste de mots
        self.etat = "-" * len(self.mot_secret) # Créer l'état du mot avec des '-'
        self.nbr_erreur = 0 # Initialise le nombre d'erreur à 0
        self.max_erreur = 7 # Définie le nombre maximale d'erreurs
        self.lettre_entre = list()
        self.lettre_fausse = list()
        self.liste_mots_possible = Pendu_Game.mots_longueur(self.list_words, len(self.mot_secret)) # Définie le nombre de mot possible

        self.update_widget() # Mise à jour des widjets
        self.is_init = True # Indique qu'une partie à été initialisé

    
    def creat_help_window(self):
        # Fontion de création de la fenêtre 'Comment jouer ?' du menu 'Aide'
        if not self.is_help_window_creat: # Si la fenêtre d'aide n'a pas déjà été créée
            # Création de la fenêtre d'aide
            self.help_window = Toplevel(self.window)
            # Personalisation de la fenêtre d'aide
            self.help_window.title("Comment jouer ?") # Titre de la fenêtre d'aide
            self.help_window.geometry("489x480") # Taile de la fenêtre d'aide
            self.help_window.resizable(0,0) # Désactive la redimention de la fenêtre d'aide
            self.window.config(background=self.color_bg) # Arrière plan

            image = PhotoImage(file=self.path+"/assets/banniere_aide.png").subsample(2) # Charge l'image d'aide

            # Création de l'interface
            canvas=Canvas(
                self.help_window,
                bg=self.color_bg,
                width=914/3,
                height=2100/2,
                scrollregion=(0,0,0,2100/2)
                )
            canvas.create_image(950/4, 2100/4,image=image) # L'affichage de l'image

            vertibar=Scrollbar(self.help_window, orient=VERTICAL) # La scroll bar verticale
            vertibar.pack(side=RIGHT,fill=Y) # Placement de la scroll bar
            # Configuration de l'interface avec la scroll bar
            vertibar.config(command=canvas.yview)
            canvas.config(
                yscrollcommand=vertibar.set
                )
            canvas.pack(expand=True,side=LEFT,fill=BOTH) # Placement de l'image

            self.help_window.mainloop() # Affichage de la fenêtre d'aide


    def run(self):
        # Fonction qui lance le jeu
        if self.is_init: # Si une partie à été initialisée
            self.window.mainloop() # Affichage de la fenêtre 
        else: # Sinon
            raise Exception("Le jeu n'a pas été initialisez\n\tAppeler la fontion 'init_game' pour initialiser une partie") # Leve une erreur


    def get_possible_letter(self):
        # Fonction qui renvoie les lettres restantes pouvant être joué
        possible_letter = ""
        for i in range(26): # Parcour des 26 lettres de l'alphabet
            if not (chr(65+i) in self.lettre_fausse or chr(97+i) in self.lettre_entre): # Si la lettre n'est pas dans la liste des lettres fausses ou celle des lettres entrées
                possible_letter += chr(65+i).lower() + " " # Ajout de la lettre à la chaine avec un espace
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
        postconditions : liste de chaines de caractères : tous les éléments de mots qui ont la
        longueur n
        """
        word_list = list()
        for mot in liste_mots: # Parcour des mots de la liste
            if len(mot) == n: # Si la longueur du mot est celle souhaitée
                word_list.append(mot) # Ajout du mot à la liste
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
        c = c.upper() # On met le caractère en majuscule

        caractere_to_check = [c] # Liste des caractère à vérifié
        for lettre, lettre_variantes in Pendu_Game.variantes.items(): # Parcoure des variants
            if c == lettre: # Si le caractère est une lettre avec des variant
                caractere_to_check = list() # On vide la liste
                # On ajoute toute les caractères variants à la liste des caractère à vérifié
                for caractere in lettre_variantes:
                    caractere_to_check.append(caractere)
                break # On sort de la boucle

        for i in range( len(mot) ): # Parcour du mot (on parcour ici la longueur du mot)
            for caractere in caractere_to_check: # Parcour de la liste des caractère à vérifié
                if caractere == mot[i]: # Si le carctère est le même que celui du mot
                    etat = etat[:i] + caractere + etat[i+1:] # Ajout du carctère à l'état
        return etat


    @staticmethod
    def get_possible_word(liste_mots, impossible_letter, etat):
        # Fonction renvoyant la liste des mots possible en fonction de l'état
        
        # On compte le nombre de fois que chaque lettre apparaît dans l'état
        etat_lettre_contenant = dict()
        for lettre in etat: # Parcoure de l'état
            if lettre != '-': # Si le caractère n'est pas un '-'
                if etat_lettre_contenant.get(lettre): # Si le caractère est déjà dans le dictionnaire
                    etat_lettre_contenant[lettre] = etat_lettre_contenant[lettre] + 1 # On ajoute une apparition
                else: etat_lettre_contenant[lettre] = 1 # Sinon on ajoute la lettre
                # Fonction définisant les lettres impossible (par exemple si l'état contient seulement un 'E' comme avec '-E---', il est donc impossible que l'état est l'une de ses variantes)
                for value in Pendu_Game.variantes.values(): # Parcoure des chaines des variants
                    for i in range(len(value)): # Parcoure des variants
                        if lettre == value[i]: # Si la lettre est une variante
                            str_impossible_letter = value[:i] + value[i+1:] # On définie une chaine contenant les autres variants
                            for letter_bis in str_impossible_letter: # Parcoure de la chaine
                                if not letter_bis in impossible_letter: # Si la variante n'est pas dans la liste des lettres impossibles
                                    impossible_letter.append(letter_bis) # On l'ajoute
        # Boucle vérifiant que les lettres de l'état ne soit pas présent dans la liste des lettres impossibles
        for key in etat_lettre_contenant.keys():
            if key in impossible_letter: impossible_letter.remove(key)

        words_possible = list()
        for mot in liste_mots: # Parcoure de chaque mot de la liste
            mot_lettre_contenant = dict()
            # On compte le nombre de fois que chaque lettre apparaît dans le mot
            for lettre in mot: # Parcoure du mot
                if mot_lettre_contenant.get(lettre): # Si le caractère est déjà dans le dictionnaire
                    mot_lettre_contenant[lettre] = mot_lettre_contenant[lettre] + 1 # On ajoute une apparition
                else:  mot_lettre_contenant[lettre] = 1 # Sinon on ajoute la lettre
            is_possible = True
            for lettre in mot: # Parcoure du mot
                if lettre in impossible_letter: # Si une de ses lettres est parmis celle des lettres impossible
                    is_possible = False # Le mot est noté impossible
                    break
            if is_possible: # Si le mot à passé le test précédent
                for key, value in etat_lettre_contenant.items(): # Parcoure du nombre d'appariton des lettres de l'état
                    if mot_lettre_contenant.get(key): # Si le mot contient la même lettre
                        if mot_lettre_contenant[key] == value: # Et en même quantité
                            continue # On passe à la lettre suivante
                    is_possible = False # Si il échoue au test il est noté impossible
                    break
            if is_possible: # Si le mot à passé les deux tests précédent
                for i in range(len(mot)): # Parcour du mot (on parcour ici la longueur du mot)
                    if etat[i] != '-': # Si la lettre de l'état correspondant n'est pas un '-'
                        if mot[i] != etat[i]: # Si la lettre n'est pas la même 
                            is_possible = False # On le note impossible
                            break
            if is_possible: words_possible.append(mot) # Si le mot est noté possible on l'ajoute à la liste des mots possible
        return words_possible

    @staticmethod
    def is_variant(caractere):
        # Fontion vérifiant si le caractère est un variant
        for cle in Pendu_Game.variantes: # Parcoure des variannts
            if caractere != cle and caractere in Pendu_Game.variantes[cle]: # Si le caractère n'est pas une lettre de l'alphabet et est une variante
                return True # On renvoie True
        return False # Sinon on renvoie False

    
    def print_label_console(self, _text):
        # Fonction permettant d'afficher un message dans le label de dialogue
        self.label_console.config(text=_text)


    def update_widget(self):
        # Met à jour les composant graphique avec les variables mises à jour
        self.label_info_nbr_mot.config(text=f"Nombre de mot possible: {len(self.liste_mots_possible)}")
        self.label_etat.config(text=self.etat)
        self.label_lettres.config(text=self.get_possible_letter())
        self.label_image.config(image=self.pendu_images[self.nbr_erreur])
        self.entry_letter.delete(0, 'end')


    def end_game(self):
        # Fontion appelé si le jeu est terminé
        if self.etat == self.mot_secret: # Si le mot secret à été trouvé
                self.print_label_console("Gagné ! Vous avez trouvé le mot secret ! ")
        else: # Sinon
            self.print_label_console(f"Perdu !\nLe mot secret était {self.mot_secret}")
    

    def update(self):
        # Fontion appelé pour mettre à jour le jeu
        if self.etat != self.mot_secret and self.nbr_erreur < self.max_erreur: # Si le mot secret n'a pas été trouvé et que le joueur n'a pas dépassé le nombre d'erreur maximale 
            # Récupère la saisie du joueur
            caractere = self.entry_letter.get()

            # Vérifie que la saisie soit correct
            if len(caractere) != 1: # Si la saisie est un caractère
                self.print_label_console("Entrez seulement un caractère !")
            elif caractere == " " or not caractere.isalpha() or Pendu_Game.is_variant(caractere.upper()): # Si c'est une lettre non variante
                self.print_label_console("Entrez une lettre !")
            elif caractere in self.lettre_entre: # Si elle n'a pas déjà été entré
                self.print_label_console("Vous avez déjà entré cette lettre !")
            else: # Alors
                self.lettre_entre.append(caractere) # Ajout du caractère dans la liste des caractères déjà entrer

                # Redifinition de l'état avec le caractère saisie
                etat2 = Pendu_Game.nouvel_etat( self.mot_secret, self.etat, caractere)

                if etat2 == self.etat: # Si le caractère n'est pas présent dans le mot secret
                    self.print_label_console("Dommage ...")
                    self.lettre_fausse.append(caractere.upper()) # Ajout de la lettre dans les lettre fausses
                    self.nbr_erreur += 1 # Ajout d'une erreur
                else: # Si il est présent
                    self.print_label_console("Correct !")
                    self.etat = etat2 # On redéfinie l'état à celui redéfinie avant
                # Récupère les mots possibles
                self.liste_mots_possible = Pendu_Game.get_possible_word(self.liste_mots_possible, self.lettre_fausse, self.etat)
            # Mise à jour des widjets
            self.update_widget()
            if self.nbr_erreur >= self.max_erreur: # Si le nombre d'erreur à été dépassé
                self.end_game() # On met fin à la partie
        else: # Si le mot secret à été trouvé ou que le joueur est dépassé le nombre maximale d'erreur
            self.end_game() # On met fin à la partie

            


game = Pendu_Game(bg='#F9F9F9') # Création d'une partie
game.run() # On lance le jeu
