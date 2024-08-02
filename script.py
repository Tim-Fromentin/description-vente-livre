from enum import Enum


class Langue(Enum):
    Francais = 1
    Anglais = 2
    Espagnol = 3
    Allemand = 4


class Etat(Enum):
    Neuf = 1
    Tres_satisfaisant = 2
    Satisfaisant = 3
    Abime = 4


def enregistrer():
    # Demander à l'utilisateur de remplir les informations
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    edition = input("Edition : ")
    annee = input("Année : ")
    
    # Demander à l'utilisateur de saisir un nombre pour la langue et l'état
    langue_num = int(input("Langue (1 pour Français, 2 pour Anglais, 3 pour Espagnol, 4 pour Allemand) : "))
    etat_num = int(input("Etat (1 pour Neuf, 2 pour Très satisfaisant, 3 pour Satisfaisant, 4 pour Abîmé) : "))
    
    # Convertir les numéros en objets Enum correspondants
    langue_enum = Langue(langue_num)
    etat_enum = Etat(etat_num)
    
    resume = input("Résumé : ")
    prix = input("Prix : ")
    ref = input("Référence : ")
    
    # Création du contenu du fichier texte
    contenu = f"{titre} de {auteur} éditions {edition} {annee}\nLangue : {langue_enum.name}\nÉtat : {etat_enum.name}\nRésumé : {resume}\nPrix de : {prix} hors frais de port\nRéférence : {ref}"
    
    # Enregistrement du fichier texte
    try:
        with open(f"{ref}.txt", "w", encoding="utf-8") as f:
            f.write(contenu)
            print("Annonce enregistrée avec succès")
    except:
        print("Erreur lors de l'enregistrement de l'annonce")


# Test de la fonction enregistrer
enregistrer()
