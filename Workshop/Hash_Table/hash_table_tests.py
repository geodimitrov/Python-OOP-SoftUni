import unittest
from Workshop.Hash_Table.hash_table import HashTable


class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_hash_table_init__expect_correct_attributes(self):
        self.assertEqual(4, len(self.hash_table))
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))

    def test_hash_table_length_prop__expect_correct_result(self):
        self.hash_table["Key1"] = "value1"
        self.assertEqual(1, self.hash_table.length)

    def test_hash_table_get__expect_correct_result(self):
        self.hash_table["Key1"] = "value1"
        self.assertEqual("value1", self.hash_table["Key1"])

    def test_hash_table_add__expect_execution(self):
        self.hash_table.add("Key1", "value1")
        self.assertIn("Key1", self.hash_table.keys)
        self.assertIn("value1", self.hash_table.values)

    def test_hash_table_repr__expect_correct_result(self):
        self.hash_table["Key1"] = "value1"
        expected_repr = "Key1: value1"
        actual_repr = self.hash_table.__repr__()
        self.assertEqual(expected_repr, actual_repr)