#!/usr/bin/python3
"Modules"
import unittest
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class Plase Test"""
    
    def test_noArg(self):
        self.assertEqual(Place, type(Place()))

    def test_newInstance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Place().id))


if __name__ == "__main__":
    unittest.main()
