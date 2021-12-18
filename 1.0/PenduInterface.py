import os
from tkinter import *


class PenduWindow:

    def __init__(self):
        self.window = Tk()

        self.pendu_images = [PhotoImage(file=os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+f"/assets/{i}.png").subsample(2) for i in range(1, 9)]
        self.index_image = 0

        self.window.title("Pendu !") # Titre de la fenêtre
        self.window.iconbitmap(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+"/assets/icon.ico") # Icône de la fenêtre
        self.window.config(background='#FFFFFF') # Arrière plan

        # Taille et position de la fenêtre
        width, height = 720, 480 # Taille de la fenêtre
        left_pos = (self.window.winfo_screenwidth() - width) / 2 # Position par raport à la gauche de l'écran
        top_pos = (self.window.winfo_screenheight() - height) / 4 # Position par raport à la droite de l'écran
        self.window.geometry( "%dx%d+%d+%d" % (width, height, left_pos, top_pos)) # Application de la taille et de la position
        self.window.resizable(0,0)

        self.frame_top = Frame(self.window)
        self.title = Label(self.frame_top, text="Pendu !", font=("Courrier", 25))

        self.frame_middle = Frame(self.window)
        self.label_etat = Label(self.frame_middle, text="-----", font=("Courrier"))
        self.label_info_nbr_mot = Label(self.frame_middle, text="Nombre de mot possible: 2071")
        self.entry_letter = Entry(self.frame_middle)
        self.entry_boutton = Button(self.frame_middle, text="Entrer", font=("Courrier"))

        self.frame_buttom = Frame(self.window)
        self.label_image = Label(self.frame_buttom, width=150, height=150 , bg="#FFFFFF", image=self.pendu_images[self.index_image])
        self.frame_info_lettre = Frame(self.frame_buttom)
        self.label_info_lettres = Label(self.frame_info_lettre, text="Lettre possible:", font=("Courrier", 20))
        self.label_lettres = Label(self.frame_info_lettre, text="a b c d e f g h i j k l m n o p q r s t u v w x y z", font=("Courrier", 10))

        
        self.title.pack(expand=YES, fill=X)
        self.frame_top.pack(fill=X)

        self.g = Frame(self.window)
        self.g.pack(expand=YES, fill=X)

        self.label_etat.grid(row=0, column=1)
        self.label_info_nbr_mot.grid(row=1, column=0)
        self.entry_letter.grid(row=1, column=1, padx=125)
        self.entry_boutton.grid(row=1, column=2)
        self.frame_middle.pack(expand=YES, fill=X)

        self.console_frame = Frame(self.window)
        self.label = Label(self.console_frame, width=720)
        self.label.pack(fill=X)
        self.console_frame.pack(expand=YES, fill=Y)


        self.label_image.grid(row=0, column=0)
        self.frame_info_lettre.grid(row=0, column=1)
        self.label_info_lettres.pack(padx=150)
        self.label_lettres.pack()
        self.frame_buttom.pack(expand=YES, fill=X)
        

        self.window.mainloop()


PenduWindow()