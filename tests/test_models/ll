#!/usr/bin/python3
"Modules"
import models
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(City, type(City()))

    def test_new(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(City().id))

    def test_city(self):
        li = City()
        self.assertEqual(str, type(City.city_id))
        self.assertIn("city_id", dir(li))
        self.assertNotIn("city_id", li.__dict__)

    def test_user(self):
        li = City()
        self.assertEqual(str, type(City.user_id))
        self.assertIn("user_id", dir(li))
        self.assertNotIn("user_id", li.__dict__)

    def test_name(self):
        li = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = City()
        self.assertEqual(int, type(City.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = City()
        self.assertEqual(int, type(City.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = City()
        self.assertEqual(float, type(City.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = City()
        self.assertEqual(list, type(City.amenity_ids))
        self.assertIn("amenity_ids", dir(li))
        self.assertNotIn("amenity_ids", li.__dict__)

    def test_unique(self):
        k = City()
        li = City()
        self.assertNotEqual(k.id, li.id)
        
    def test_max(self):
        pl = City()
        self.assertEqual(int, type(City.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = City()
        self.assertEqual(int, type(City.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = City()
        self.assertEqual(float, type(City.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
