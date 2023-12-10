#!/usr/bin/python3
"Modules"
import models
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_Amenity(self):
        li = Amenity()
        self.assertEqual(str, type(Amenity.Amenity_id))
        self.assertIn("Amenity_id", dir(li))
        self.assertNotIn("Amenity_id", li.__dict__)

    def test_Amenity(self):
        li = Amenity()
        self.assertEqual(str, type(Amenity.Amenity_id))
        self.assertIn("Amenity_id", dir(li))
        self.assertNotIn("Amenity_id", li.__dict__)

    def test_name(self):
        li = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = Amenity()
        self.assertEqual(int, type(Amenity.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = Amenity()
        self.assertEqual(int, type(Amenity.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = Amenity()
        self.assertEqual(float, type(Amenity.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = Amenity()
        self.assertEqual(list, type(Amenity.Amenity_ids))
        self.assertIn("Amenity_ids", dir(li))
        self.assertNotIn("Amenity_ids", li.__dict__)

    def test_unique(self):
        k = Amenity()
        li = Amenity()
        self.assertNotEqual(k.id, li.id)

    def test_max(self):
        pl = Amenity()
        self.assertEqual(int, type(Amenity.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = Amenity()
        self.assertEqual(int, type(Amenity.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = Amenity()
        self.assertEqual(float, type(Amenity.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
