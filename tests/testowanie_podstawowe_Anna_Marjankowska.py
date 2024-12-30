import unittest
from unittest.mock import mock_open, patch
from flask.testing import FlaskClient
import hypothesis.strategies as st
from hypothesis import given
import requests
import threading

def add(a, b):
    return a + b

def is_palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

def divide(a, b):
    if b != 0:
        return a / b 
    else: 
        raise ValueError("Nie dziel przez zero, kolego!")
    
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

import requests
def get_weather(city):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dummy_api_key")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError("Błąd połączenia z API") from e

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"}), 200

import threading
def process_data(data):
    results = []
    def process_element(element):
        # Przykładowe przetwarzanie
        results.append(element * 2)

    threads = []
    for item in data:
        thread = threading.Thread(target=process_element, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def reverse_string(s):
    return s[::-1]

class TestAddFunction(unittest.TestCase):

    def test_integers(self):
        # Test dla liczb całkowitych
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_floats(self):
        # Test dla liczb zmiennoprzecinkowych
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_negatives(self):
        # Test dla liczb ujemnych
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-10, 5), -5)

class TestIsPalindromeFunction(unittest.TestCase):

    def test_case_insensitivity(self):
        # Test palindromów z wielkimi i małymi literami
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("RaceCar"))

    def test_with_spaces(self):
        # Test stringów z spacjami
        self.assertTrue(is_palindrome("a man a plan a canal panama"))
        self.assertTrue(is_palindrome("nurses run"))

    def test_not_palindromes(self):
        # Test stringów nie będących palindromami
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

class TestDivideFunction(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 2), -3)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()

