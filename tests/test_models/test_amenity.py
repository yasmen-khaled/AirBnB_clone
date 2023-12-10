import unittest
import models
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    def setup_amen(self):
        self.amenity = Amenity()
        self.amenity.name = "Bob"
        self.amenity.number = "1"
        amenity_dict = self.amenity.to_dict()


    def tearDown(self):
        del self.amenity

    def test_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance(self):

        self.assertIn(Amenity(), models.storage.all().values())
    def test_init(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "Bob")

    def test_str(self):
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn(self.amenity.id, amenity_str)
        self.assertIn(str(self.amenity.__dict__), amenity_str)

class TestAmenity_to_dict(unittest.TestCase):

    def setup(self):
        self.amenity = Amenity()
        self.amenity.name = "Bob"
        self.amenity.number = "1"
        amenity_dict = self.amenity.to_dict()

    def test_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_keys(self):
        self.assertIn("id", self.amenity.to_dict())
        self.assertIn("created_at", self.amenity.to_dict())
        self.assertIn("updated_at", self.amenity.to_dict())
        self.assertIn("__class__", self.amenity.to_dict())

    def test_added_attributes(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], self.amenity.name)
        self.assertEqual(amenity_dict["number"], self.amenity.number)

    def test_attributes_type(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict["id"]), str)
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)

    def test_output(self):
        dt = datetime.today()
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.amenity.id = "1-2-3-4"
        self.assertEqual(amenity_dict["created_at"],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], self.amenity.name)
