#!/usr/bin/python3
"""Modules"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_i(unittest.TestCase):
    """UnittestsState class."""

    def test_no(self):
        self.assertEqual(State, type(State()))

    def test_new(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name(self):
        set = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(set))
        self.assertNotIn("name", set.__dict__)

    def test_two(self):
        set1 = State()
        set2 = State()
        self.assertNotEqual(set1.id, set2.id)

    def test_two_states(self):
        set1 = State()
        sleep(0.05)
        set2 = State()
        self.assertLess(set1.created_at, set2.created_at)

    def test_two_sta(self):
        set1 = State()
        sleep(0.05)
        set2 = State()
        self.assertLess(set1.updated_at, set2.updated_at)

    def test_str(self):
        det = datetime.today()
        det_repr = repr(det)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = det
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + det_repr, ststr)
        self.assertIn("'updated_at': " + det_repr, ststr)

    def test_args(self):
        set = State(None)
        self.assertNotIn(None, set.__dict__.values())

    def test_instantiation(self):
        det = datetime.today()
        det_iso = det.isoformat()
        st = State(id="345", created_at=det_iso, updated_at=det_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.created_at, det)
        self.assertEqual(st.updated_at, det)

    def test_instantiation_with(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
