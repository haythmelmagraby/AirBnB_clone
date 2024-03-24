#!/usr/bin/python3
""" test base module """
import unittest
import models
from models.base_model import BaseModel


class TestBasicModel(unittest.TestCase):
    """ calss test basic model """
    def test_init(self):
        """ test initialization """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_string(self):
        base_model = BaseModel()
        self.assertTrue(str(base_model).startswith("[BaseModel]"))
        self.assertIn(base_model.id, str(base_model))
        self.assertIn(str(base_model.__dict__), str(base_model))


if __name__ == "__main__":
    unittest.main()
