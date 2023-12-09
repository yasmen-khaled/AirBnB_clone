#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests BaseModel class."""

    def test_tes(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_ects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        li = BaseModel()
        lim = BaseModel()
        self.assertNotEqual(li.id, lim.id)

    def test_created_at(self):
        li = BaseModel()
        sleep(0.05)
        lim = BaseModel()
        self.assertLess(li.created_at, lim.created_at)

    def test_updated_at(self):
        li = BaseModel()
        sleep(0.05)
        lim = BaseModel()
        self.assertLess(li.updated_at, lim.updated_at)

    def test_unused(self):
        li = BaseModel(None)
        self.assertNotIn(None, li.__dict__.values())

    def test_i_kwargs(self):
        li = datetime.today()
        dt_iso = li.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, li)
        self.assertEqual(bm.updated_at, li)

    def test_in(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_i(self):
        li = datetime.today()
        so = li.isoformat()
        ll = BaseModel("12", id="345", created_at=so, updated_at=so)
        self.assertEqual(ll.id, "345")
        self.assertEqual(ll.created_at, li)
        self.assertEqual(ll.updated_at, li)


class TestBaseModelS(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        li = BaseModel()
        sleep(0.05)
        first_updated_at = li.updated_at
        li.save()
        self.assertLess(first_updated_at, li.updated_at)


class TestBaseModelto_dict(unittest.TestCase):
    """BaseModel test to dict"""

    def test_to_dict_type(self):
        li = BaseModel()
        self.assertTrue(dict, type(li.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        li = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", li .to_dict())
        self.assertIn("updated_at",li.to_dict())
        self.assertIn("__class__", li.to_dict())

    def test_to_dict_contains_added_attributes(self):
        li = BaseModel()
        li.name = "Holberton"
        li.my_number = 98
        self.assertIn("name", li.to_dict())
        self.assertIn("my_number", li.to_dict())


if __name__ == "__main__":
    unittest.main()
