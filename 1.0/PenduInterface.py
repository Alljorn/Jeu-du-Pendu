import os
from tkinter import *


# Création de la fenêtre
window = Tk()

# Personnalisation de la fenêtre
window.title("Pendu !") # Titre de la fenêtre
window.geometry("720x480") # Taille de la fenêtre
window.maxsize(1080, 720) # Taille maximale de la fenêtre
window.minsize(720, 480) # Taille minimale de la fenêtre
window.iconbitmap(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+"/assets/icon.ico") # Icône de la fenêtre
window.config(background='#F0F0F0') # Arrière plan


canvas_image = Canvas(window, bg="#F0F0F0")
image = PhotoImage(file=os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')+"/assets/1.png")
canvas_image.create_image(300,300,image=image)


canvas_image.pack()


# Affichage de la fenêtre
window.mainloop()
