#!/usr/bin/python3
"""Modules"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests City class"""

    def test_a(self):
        self.assertEqual(City, type(City()))

    def test_b(self):
        self.assertIn(City(), models.storage.all().values())

    def test_c(self):
        self.assertEqual(str, type(City().id))

    def test_d(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_e(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_f(self):
        cl = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cl))
        self.assertNotIn("state_id", cl.__dict__)

    def test_g(self):
        cl = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cl))
        self.assertNotIn("name", cl.__dict__)

    def test_h(self):
        cl1 = City()
        cl2 = City()
        self.assertNotEqual(cl1.id, cl2.id)

    def test_i(self):
        cl1 = City()
        sleep(0.05)
        cl2 = City()
        self.assertLess(cl1.created_at, cl2.created_at)

    def test_j(self):
        cl1 = City()
        sleep(0.05)
        cl2 = City()
        self.assertLess(cl1.updated_at, cl2.updated_at)

    def test_k(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_l(self):
        cl = City(None)
        self.assertNotIn(None, cl.__dict__.values())

    def test_m(self):
        dl = datetime.today()
        dl_iso = dt.isoformat()
        cl = City(id="345", created_at=dl_iso, updated_at=dl_iso)
        self.assertEqual(cl.id, "345")
        self.assertEqual(cl.created_at, dl)
        self.assertEqual(cl.updated_at, dl)

    def test_n(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
