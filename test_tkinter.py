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


# Creation d'une frame
frame1 = Frame(window, bg="#F0F0F0", bd=1, relief=SUNKEN)

# Création de composants texte
label_title = Label(frame1, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#F0F0F0', fg='black')
label_title.pack()

label_title = Label(frame1, text="Comment allez-vous ?", font=("Courrier", 25), bg='#F0F0F0', fg='black')
label_title.pack()

# Affichage du frame
frame1.pack(expand=YES)

# Création d'un bouton
button = Button(frame1, text="Click me !", font=("Courrier", 25), bg='#F0F0F0', fg='black')
button.pack(pady=25, fill=X)


# Affichage de la fenêtre
window.mainloop()
