from city_functions import format_city_country
import unittest


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Check if names like "Zacatecas, Mexico" work"""

        formatted_name = format_city_country('zacatecas', 'mexico')
        self.assertEqual(formatted_name, "Zacatecas, Mexico")

    def test_city_country_population(self):
        """Check if formatted text when population provided is correct."""

        formatted_text = format_city_country('zacatecas', 'mexico', 200_000)
        self.assertEqual(
            formatted_text, 'Zacatecas, Mexico - population 200000')


if __name__ == '__main__':
    unittest.main()
