#!/usr/bin/python3
"Modules"
import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(User, type(User()))

    def test_new(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_User(self):
        li = User()
        self.assertEqual(str, type(User.User_id))
        self.assertIn("User_id", dir(li))
        self.assertNotIn("User_id", li.__dict__)

    def test_user(self):
        li = User()
        self.assertEqual(str, type(User.user_id))
        self.assertIn("user_id", dir(li))
        self.assertNotIn("user_id", li.__dict__)

    def test_name(self):
        li = User()
        self.assertEqual(str, type(User.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = User()
        self.assertEqual(int, type(User.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = User()
        self.assertEqual(int, type(User.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = User()
        self.assertEqual(float, type(User.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = User()
        self.assertEqual(list, type(User.amenity_ids))
        self.assertIn("amenity_ids", dir(li))
        self.assertNotIn("amenity_ids", li.__dict__)

    def test_unique(self):
        k = User()
        li = User()
        self.assertNotEqual(k.id, li.id)
        
    def test_max(self):
        pl = User()
        self.assertEqual(int, type(User.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = User()
        self.assertEqual(int, type(User.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = User()
        self.assertEqual(float, type(User.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
