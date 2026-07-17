import unittest
from name import get_full_name


class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name("ibroxim", "raxmatullayev")
        self.assertEqual(name, "Ibroxim Raxmatullayev")

    def test_otasining_ismi(self):
        name = get_full_name("ibroxim", "raxmatullayev", "farxod o'g'li")
        self.assertEqual(name, "Ibroxim Farxod O'G'Li Raxmatullayev")


unittest.main()
