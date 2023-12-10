#!/usr/bin/python3
"Modules"
import models
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(Place, type(Place()))

    def test_new(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Place().id))

    def test_city(self):
        li = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(li))
        self.assertNotIn("city_id", li.__dict__)

    def test_user(self):
        li = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(li))
        self.assertNotIn("user_id", li.__dict__)

    def test_name(self):
        li = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(li))
        self.assertNotIn("amenity_ids", li.__dict__)

    def test_unique(self):
        k = Place()
        li = Place()
        self.assertNotEqual(k.id, li.id)

    def test_max(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
