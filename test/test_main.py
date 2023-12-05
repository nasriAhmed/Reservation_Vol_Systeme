import unittest
from script.main import Avion, Passager
class TestSystemeReservationVol(unittest.TestCase):
    def setUp(self):
        self.avion1 = Avion("AF123", (5, 4), "A")
        self.passager1 = Passager("Ahmed")
        self.passager2 = Passager("Youssef")

    def test_initialisation_avion(self):
        #Vérifier l'initialisation correcte de l'avion
        self.assertEqual(self.avion1.numero_vol, "AF123")
        self.assertEqual(self.avion1.taille, (5, 4))
        self.assertEqual(self.avion1.disposition, "A")
        self.assertEqual(len(self.avion1.places_disponibles), 20)

    def test_reservation_place(self):
        #Vérifier que la réservation d'une place fonctionne correctement
        self.avion1.reserver_place(self.passager1, "1A")
        self.assertIn("1A", self.passager1.reservations["AF123"])
        self.assertNotIn("1A", self.avion1.places_disponibles)        
    def test_reservation_place_deja_prise(self):
        #Vérifier qu'une tentative de double réservation génère une exception
        self.avion1.reserver_place(self.passager1, "1A")
        with self.assertRaises(ValueError):
            self.avion1.reserver_place(self.passager2, "1A")

    def test_afficher_reservations_passager(self):
        # Vérifier que l'affichage des réservations du passager fonctionne correctement
        self.avion1.reserver_place(self.passager1, "1A")
        self.passager1.afficher_reservations()
        self.assertEqual(len(self.passager1.reservations["AF123"]), 1)

    def test_afficher_places_disponibles_apres_reservation(self):
        # Vérifier que le nombre de places disponibles est correct après une réservation
        self.avion1.reserver_place(self.passager1, "1A")
        self.assertEqual(len(self.avion1.places_disponibles), 19)

    def test_modifier_siege_passager(self):
        # Vérifier la modification correcte d'un siège pour un passager
        self.avion1.reserver_place(self.passager1, "1A")
        self.avion1.reserver_place(self.passager2, "2B")
        self.avion1.modifier_siege_passager(self.passager1, "1A", "3C")
        self.assertIn("3C", self.passager1.reservations["AF123"])
        self.assertNotIn("1A", self.passager1.reservations["AF123"])
        self.assertIn("1A", self.avion1.places_disponibles)
        self.assertNotIn("3C", self.avion1.places_disponibles)
    def test_double_reservation(self):
        #Vérifier la gestion appropriée de la modification de siège avec un nouveau siège déjà réservé
        avion = Avion("AF123", (5, 4), "A")
        passager1 = Passager("Ahmed")

        avion.reserver_place(passager1, "1A")
        avion.afficher_places_disponibles()

        with self.assertRaises(ValueError):
            avion.reserver_place(passager1, "1A")

if __name__ == '__main__':
    unittest.main()