import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does city_country return a properly formatted string?"""
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()
