#!/usr/bin/python3
"""Modules"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_i(unittest.TestCase):
    """Unittests file class."""

    def test_FileStorage_inst(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_fil(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_m(unittest.TestCase):
    """UnittestsFileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_ne(self):
        bem = BaseModel()
        ues = User()
        set = State()
        pel = Place()
        cey = City()
        aem = Amenity()
        rev = Review()
        models.storage.new(bem)
        models.storage.new(ues)
        models.storage.new(set)
        models.storage.new(pel)
        models.storage.new(cey)
        models.storage.new(aem)
        models.storage.new(rev)
        self.assertIn("BaseModel." + bem.id, models.storage.all().keys())
        self.assertIn(bem, models.storage.all().values())
        self.assertIn("User." + ues.id, models.storage.all().keys())
        self.assertIn(ues, models.storage.all().values())
        self.assertIn("State." + set.id, models.storage.all().keys())
        self.assertIn(set, models.storage.all().values())
        self.assertIn("Place." + pel.id, models.storage.all().keys())
        self.assertIn(pel, models.storage.all().values())
        self.assertIn("City." + cey.id, models.storage.all().keys())
        self.assertIn(cey, models.storage.all().values())
        self.assertIn("Amenity." + aem.id, models.storage.all().keys())
        self.assertIn(aem, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def test_nw(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_s(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_saveg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_rel(self):
        bem = BaseModel()
        ues = User()
        set = State()
        pel = Place()
        cey = City()
        aem = Amenity()
        rev = Review()
        models.storage.new(bem)
        models.storage.new(ues)
        models.storage.new(set)
        models.storage.new(pel)
        models.storage.new(cey)
        models.storage.new(aem)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bem.id, objs)
        self.assertIn("User." + ues.id, objs)
        self.assertIn("State." + set.id, objs)
        self.assertIn("Place." + pel.id, objs)
        self.assertIn("City." + cey.id, objs)
        self.assertIn("Amenity." + aem.id, objs)
        self.assertIn("Review." + rev.id, objs)

    def test_relg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
