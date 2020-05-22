""" Unit Test für Maximum """
import unittest
from statistik import get_max

class TestGetMax(unittest.TestCase):
    """ Unittests für get_max(list) """
    def test_get_max(self):
        """ Basistest: valide Eingaben """
        liste = [3, -12, 4, 12, -4, 65, 4, 7]
        self.assertEqual(65, get_max(liste), "Liste mit positiven und negativen Elementen")
        self.assertEqual(5, get_max([5]), "Liste mit einem Element")
        self.assertEqual(12, get_max([3, 4, 11, 5, 12]),
                         "Liste mit positiven ganzen Zahlen, Maximum ist das letzte Element")
        self.assertEqual(101.3, get_max([101.3, 55.5]), "Liste mit Gleitkommazahlen")
        self.assertEqual(-5, get_max([-10, -5, -9]), "Liste mit negativen Zahlen")

    def test_values(self):
        """ Fehleingaben: leere Liste erzeugt Ausnahme """
        self.assertRaises(ValueError, get_max, [])

    def test_types(self):
        """ Fehleingaben: Listelemente enthalten falsche Datentype(bool, Strings) """
        self.assertRaises(ValueError, get_max, [1, 'a', "masder"])
        self.assertRaises(ValueError, get_max, [True, False])

if __name__ == '__main__':
    unittest.main()
