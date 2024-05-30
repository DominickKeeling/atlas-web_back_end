#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and understand
its purpose. Play with it in the Python console to make sure you understand.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    test access nested map with key path
    """
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the method returns what its supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map function with exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class for testing get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Testing get_json function
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get') as mock_get:

            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Class for testing memoize function
    """

    def test_memoize(self):
        """
        Test memoize function
        """

        class TestClass:
            """
            Test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(
                test_instance, 'a_method', return_value=42) as mock_method:

            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            mock_method.assert_called_once_with()
