import tkinter as tk

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Ma Présentation")
fenetre.geometry("600x400")

# Titre
titre = tk.Label(
    fenetre,
    text="Bienvenue dans ma présentation",
    font=("Arial", 20)
)
titre.pack(pady=20)

# Texte
texte = tk.Label(
    fenetre,
    text="Je découvre Python et les interfaces graphiques !",
    font=("Arial", 14)
)
texte.pack(pady=20)

# Fonction bouton
def message():
    texte.config(text="Bravo ! Tu viens de cliquer sur le bouton.")

# Bouton
bouton = tk.Button(
    fenetre,
    text="Clique ici",
    command=message,
    font=("Arial", 14)
)
bouton.pack(pady=20)

# Lancer l'application
fenetre.mainloop()