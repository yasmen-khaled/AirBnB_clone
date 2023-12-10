#!/usr/bin/python3
"Modules"
import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class Plase Test"""

    def test_no(self):
        self.assertEqual(Review, type(Review()))

    def test_new(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_Review(self):
        li = Review()
        self.assertEqual(str, type(Review.Review_id))
        self.assertIn("Review_id", dir(li))
        self.assertNotIn("Review_id", li.__dict__)

    def test_user(self):
        li = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(li))
        self.assertNotIn("user_id", li.__dict__)

    def test_name(self):
        li = Review()
        self.assertEqual(str, type(Review.name))
        self.assertIn("name", dir(li))
        self.assertNotIn("name", li.__dict__)

    def test_n(self):
        li = Review()
        self.assertEqual(int, type(Review.number_rooms))
        self.assertIn("number_rooms", dir(li))
        self.assertNotIn("number_rooms", li.__dict__)

    def test_number(self):
        pl = Review()
        self.assertEqual(int, type(Review.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_longitude(self):
        li = Review()
        self.assertEqual(float, type(Review.longitude))
        self.assertIn("longitude", dir(li))
        self.assertNotIn("longitude", li.__dict__)

    def test_attribute(self):
        li = Review()
        self.assertEqual(list, type(Review.amenity_ids))
        self.assertIn("amenity_ids", dir(li))
        self.assertNotIn("amenity_ids", li.__dict__)

    def test_unique(self):
        k = Review()
        li = Review()
        self.assertNotEqual(k.id, li.id)
        
    def test_max(self):
        pl = Review()
        self.assertEqual(int, type(Review.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price(self):
        li = Review()
        self.assertEqual(int, type(Review.price_by_night))
        self.assertIn("price_by_night", dir(li))
        self.assertNotIn("price_by_night", li.__dict__)

    def test_latitude(self):
        li = Review()
        self.assertEqual(float, type(Review.latitude))
        self.assertIn("latitude", dir(li))
        self.assertNotIn("latitude", li.__dict__)

    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
