#!/usr/bin/python3
"Modules"
import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(State, type(State()))

    def test_new(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_State(self):
        li = State()
        self.assertEqual(str, type(State.State_id))
        self.assertIn("State_id", dir(li))
        self.assertNotIn("State_id", li.__dict__)

    def test_user(self):
        li = State()
        self.assertEqual(str, type(State.user_id))
        self.assertIn("user_id", dir(li))
        self.assertNotIn("user_id", li.__dict__)

    def test_name(self):
        li = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = State()
        self.assertEqual(int, type(State.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = State()
        self.assertEqual(int, type(State.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = State()
        self.assertEqual(float, type(State.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = State()
        self.assertEqual(list, type(State.amenity_ids))
        self.assertIn("amenity_ids", dir(li))
        self.assertNotIn("amenity_ids", li.__dict__)

    def test_unique(self):
        k = State()
        li = State()
        self.assertNotEqual(k.id, li.id)
        
    def test_max(self):
        pl = State()
        self.assertEqual(int, type(State.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = State()
        self.assertEqual(int, type(State.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = State()
        self.assertEqual(float, type(State.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
