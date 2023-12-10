#!/usr/bin/python3
"""Models"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_i(unittest.TestCase):
    """Unittests Review class."""

    def test_no(self):
        self.assertEqual(Review, type(Review()))

    def test_new(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_two(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_two_reviews(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_t(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str(self):
        dl = datetime.today()
        dl_repr = repr(dl)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dl
        rvstr = rev.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dl_repr, rvstr)
        self.assertIn("'updated_at': " + dl_repr, rvstr)

    def test_args(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instantia(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dt)
        self.assertEqual(rev.updated_at, dt)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
