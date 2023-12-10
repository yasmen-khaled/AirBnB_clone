#!/usr/bin/python3
"""Modules"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_ins(unittest.TestCase):
    """Unittests Place class."""

    def test_no(self):
        self.assertEqual(Place, type(Place()))

    def test_new(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city(self):
        plee = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plee))
        self.assertNotIn("city_id", plee.__dict__)

    def test_user(self):
        ple = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(ple))
        self.assertNotIn("user_id", ple.__dict__)

    def test_name_is(self):
        ple = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(ple))
        self.assertNotIn("name", ple.__dict__)

    def test_description(self):
        ple = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(ple))
        self.assertNotIn("desctiption", ple.__dict__)

    def test_number(self):
        ple = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(ple))
        self.assertNotIn("number_rooms", ple.__dict__)

    def test_number_n(self):
        ple = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(ple))
        self.assertNotIn("number_bathrooms", ple.__dict__)

    def test_max_guest(self):
        ple = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(ple))
        self.assertNotIn("max_guest", ple.__dict__)

    def test_price(self):
        ple = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(ple))
        self.assertNotIn("price_by_night", ple.__dict__)

    def test_latitude(self):
        ple = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(ple))
        self.assertNotIn("latitude", ple.__dict__)

    def test(self):
        ple = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(ple))
        self.assertNotIn("longitude", ple.__dict__)

    def test_amenity(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_places_unique(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two(self):
        ple1 = Place()
        sleep(0.05)
        ple2 = Place()
        self.assertLess(ple1.updated_at, ple2.updated_at)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        p = Place()
        p.id = "123456"
        p.created_at = p.updated_at = dt
        pls = p.__str__()
        self.assertIn("[Place] (123456)", pls)
        self.assertIn("'id': '123456'", pls)
        self.assertIn("'created_at': " + dt_repr, pls)
        self.assertIn("'updated_at': " + dt_repr, pls)

    def test_args(self):
        ple = Place(None)
        self.assertNotIn(None, ple.__dict__.values())

    def test_instantiation(self):
        dl = datetime.today()
        dl_iso = dl.isoformat()
        ple = Place(id="345", created_at=dl_iso, updated_at=dl_iso)
        self.assertEqual(ple.id, "345")
        self.assertEqual(ple.created_at, dl)
        self.assertEqual(ple.updated_at, dl)

    def test_instantiation_with(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
