#Ce module contient la définition des classes Avion et Passager pour gérer les réservations.
class Avion:
    """
    Cette classe représente un objet Avion pour gérer les réservations de sièges.
    """
    #Initialise un objet Avion avec un numéro de vol, une taille et une disposition.
    def __init__(self, numero_vol, taille, disposition):
        self.numero_vol = numero_vol
        self.taille = taille
        self.disposition = disposition
        self.places_disponibles = self.initialiser_places()
    #Initialise la liste des places disponibles en fonction de la taille de l'avion.
    def initialiser_places(self):
        places = []
        for rang in range(1, self.taille[0] + 1):
            for siege in range(1, self.taille[1] + 1):
                places.append(f"{rang}{chr(64 + siege)}")
        return places
    #Afficher les places disponibles pour le vol
    def afficher_places_disponibles(self):
        print(f"Places disponibles pour le vol {self.numero_vol}: {', '.join(self.places_disponibles)}")
    #Réserver une place pour un passager
    def reserver_place(self, passager, place):
        if place in self.places_disponibles:
            self.places_disponibles.remove(place)
            passager.ajouter_reservation(self.numero_vol, place)
            print(f"Place {place} réservée avec succès pour {passager.nom}.")
        else:
            print(f"La place {place} est déjà réservée. Veuillez choisir une autre place.")
    #Modifier le siège réservé par un passager
    def modifier_siege_passager(self, passager, ancien_siege, nouveau_siege):
        if nouveau_siege in self.places_disponibles:
            # Retirer l'ancien siège de la liste des places disponibles avant d'ajouter le nouveau siège
            self.places_disponibles.append(ancien_siege)
            self.places_disponibles.remove(nouveau_siege)
            passager.modifier_reservation(self.numero_vol, ancien_siege, nouveau_siege)
            print(f"Siège modifié avec succès pour {passager.nom}. Nouveau siège : {nouveau_siege}.")
        else:
            print(f"Le siège {nouveau_siege} est déjà réservé. Veuillez choisir un autre siège.")     
        # Afficher les places disponibles après la modification
        self.afficher_places_disponibles()
class Passager:
    """
    Cette classe représente un objet Passager pour gérer les réservations de sièges.
    """
    def __init__(self, nom):
        #Initialise un nouvel objet Passager avec le nom fourni
        self.nom = nom
        #Dictionnaire pour stocker les réservations par numéro de vol.
        self.reservations = {}

    #Ajouter une réservation pour le passager sur un vol donné
    def ajouter_reservation(self, numero_vol, place):
        if numero_vol in self.reservations:
            self.reservations[numero_vol].append(place)
        else:
            self.reservations[numero_vol] = [place]
    #Modifier la réservation du passager d'un siège à un autre sur un vol donné.
    def modifier_reservation(self, numero_vol, ancien_siege, nouveau_siege):
        if numero_vol in self.reservations:
            self.reservations[numero_vol].remove(ancien_siege)
            self.reservations[numero_vol].append(nouveau_siege)
        else:
            print(f"Aucune réservation trouvée pour le vol {numero_vol}.")
    #Afficher les réservations du passager.
    def afficher_reservations(self):
        print(f"Réservations pour {self.nom}:")
        for numero_vol, places in self.reservations.items():
            print(f"Vol {numero_vol}: {', '.join(places)}")

# Exemple d'utilisation
if __name__ == "__main__":
    avion1 = Avion("AF123", (5, 4), "A")
    passager1 = Passager("Ahmed")
    passager2 = Passager("Youssef")

    avion1.afficher_places_disponibles()

    avion1.reserver_place(passager1, "1A")
    avion1.reserver_place(passager2, "2B")

    avion1.afficher_places_disponibles()

    passager1.afficher_reservations()
    passager2.afficher_reservations()

    # Modification de réservation pour passager1
    avion1.modifier_siege_passager(passager1, "1A", "3C")
    
    passager1.afficher_reservations()
    passager2.afficher_reservations()
    #avion1.afficher_places_disponibles()