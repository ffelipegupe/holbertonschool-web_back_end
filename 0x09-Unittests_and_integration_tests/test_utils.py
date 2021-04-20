#!/usr/bin/env python3
""" utils.py test module
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ access_nested_map test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method that tests access_nested_map function """
        self.assertEquals(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Method that tests access_nested_map's exception """
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    """ get_json test class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, class_mock):
        """ Method that tests get_json function """
        class_mock.return_value = test_payload
        self.assertEquals(get_json(test_url), test_payload)
