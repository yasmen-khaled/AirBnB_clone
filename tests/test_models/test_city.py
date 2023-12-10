#!/usr/bin/python3
"""Modules"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity_F(unittest.TestCase):
    """test for city class"""

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_inher(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_att(self):
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_def(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_st(self):
        expected_output = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_output)

    def test_empty_state_id_and_name(self):
        self.city.state_id = "CA"
        self.city.name = "San Francisco"
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_id_type(self):
        self.city.state_id = 123
        self.assertEqual(self.city.state_id, 123)

    def test_name_type(self):
        self.city.name = 123
        self.assertEqual(self.city.name, 123)

    def test_to(self):
        expected_dict = {
            'id': self.city.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            '__class__': 'City'
        }
        self.assertEqual(self.city.to_dict(), expected_dict)

    def test_state_id(self):
        self.city.state_id = ""
        self.assertEqual(self.city.state_id, "")

    def testempty_name(self):
        self.city.name = ""
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
