from tkinter import *

# Création de la fenêtre
window = Tk()

# Personnalisation de la fenêtre
window.title("Pendu !") # Titre de la fenêtre
window.geometry("720x480") # Taille de la fenêtre
window.maxsize(1080, 720) # Taille maximale de la fenêtre
window.minsize(720, 480) # Taille minimale de la fenêtre
window.iconbitmap("icon.ico") # Icône de la fenêtre
window.config(background='#F0F0F0') # Arrière plan

# Création d'une barre de menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Selctionner tout")
edit_menu.add_command(label="Annuler")
menu_bar.add_cascade(label="Edition", menu=edit_menu)

window.config(menu=menu_bar)

# Création d'un composant texte
label_title = Label(window, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#F0F0F0', fg='black')
label_title.pack()


# Affichage de la fenêtre
window.mainloop()
