#!/usr/bin/python3
"""Modules"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """class unitest ameinety"""

    def test_no(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name(self):
        amn = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amn.__dict__)

    def test_two(self):
        amn1 = Amenity()
        amn2 = Amenity()
        self.assertNotEqual(amn1.id, amn2.id)

    def test_two_amenities(self):
        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.created_at, amn2.created_at)

    def test_two_amenities_different(self):
        amn1 = Amenity()
        sleep(0.05)
        amn2 = Amenity()
        self.assertLess(amn1.updated_at, amn2.updated_at)

    def test_str(self):
        dl = datetime.today()
        dl_repr = repr(dl)
        amn = Amenity()
        amn.id = "123456"
        amn.created_at = amn.updated_at = dl
        amstr = amn.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dl_repr, amstr)
        self.assertIn("'updated_at': " + dl_repr, amstr)

    def test_args(self):
        amn = Amenity(None)
        self.assertNotIn(None, amn.__dict__.values())

    def test_instan(self):
        dl = datetime.today()
        dl_iso = dl.isoformat()
        am = Amenity(id="345", created_at=dl_iso, updated_at=dl_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dl)
        self.assertEqual(am.updated_at, dl)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
