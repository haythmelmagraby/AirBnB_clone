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

    def test_save(self):
        """ Test save """
        base_model = BaseModel()
        first_update_at = base_model.updated_at
        second_update_at = base_model.save()
        self.assertNotEqual(second_update_at, first_update_at)

    def test_to_dict(self):
        base_model = BaseModel()
        base_dict = base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base_model.id)
        self.assertEqual(base_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         base_model.updated_at.isoformat())
        self.assertEqual(base_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
