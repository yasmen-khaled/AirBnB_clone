#!/usr/bin/python3
"""Moudules"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_i(unittest.TestCase):
    """Unittests User class."""

    def test_n(self):
        self.assertEqual(User, type(User()))

    def test_new(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first(self):
        self.assertEqual(str, type(User.first_name))

    def test_last(self):
        self.assertEqual(str, type(User.last_name))

    def test_t(self):
        ues1 = User()
        ues2 = User()
        self.assertNotEqual(ues1.id, ues2.id)

    def test_two_users(self):
        ues1 = User()
        sleep(0.05)
        ues2 = User()
        self.assertLess(ues1.created_at, ues2.created_at)

    def test_two(self):
        ues1 = User()
        sleep(0.05)
        ues2 = User()
        self.assertLess(ues1.updated_at, ues2.updated_at)

    def test_str(self):
        dl = datetime.today()
        dl_repr = repr(dl)
        ues = User()
        ues.id = "123456"
        ues.created_at = ues.updated_at = dl
        usstr = ues.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dl_repr, usstr)
        self.assertIn("'updated_at': " + dl_repr, usstr)

    def test_args(self):
        ues = User(None)
        self.assertNotIn(None, ues.__dict__.values())

    def test_instant(self):
        dl = datetime.today()
        dl_iso = dl.isoformat()
        us = User(id="345", created_at=dl_iso, updated_at=dl_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dl)
        self.assertEqual(us.updated_at, dl)

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
