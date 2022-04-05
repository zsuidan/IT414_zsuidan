import unittest
from functions.regex_functions import *

class RegexTestCase(unittest.TestCase):
    """Tests for functions in the regex_functions.py file."""

    def test_valid_coords(self):
        """Here are a bunch of values I think should work"""
        valid_coords_to_test = ["4.93211, -149.91635", "-27.79793, -156.61866", "-1.23, 1.23", "1.23, 1.23"]
        
        for coord in valid_coords_to_test:
            self.assertTrue(isValidCoord(coord))

    def test_invalid_coords(self):
        """Here is a bunch of values I think should NOT work"""
        invalid_coords_to_test = [".123, 12.34", "12.34 12.34", "+12.34, +12.34", "12, 12", "abc, 12.34", "134.12, 1234.12", "123.45,123.45"]
        
        for coord in invalid_coords_to_test:
            self.assertFalse(isValidCoord(coord))

    def test_valid_dollars(self):
        """Here are a bunch of values I think should work"""
        valid_dollar_values_to_test = ["$123,456.78", "$123.45", "$1.23", "$1", "$0.50"]
        
        for value in valid_dollar_values_to_test:
            self.assertTrue(isValidDollars(value))

    def test_invalid_dollars(self):
        """Here is a bunch of values I think should NOT work"""
        invalid_dollar_values_to_test = ["123,456,78", "1234$123.45", "$123.451245", "$.12", "$123,45", "$12.1", "$12.", "-$12"]
        
        for value in invalid_dollar_values_to_test:
            self.assertFalse(isValidDollars(value))

    def test_valid_credit_card(self):
        """Here are a bunch of values I think should work"""
        valid_cards_to_test = ["1112223334445", "11122233344455", "111222333444555", "1112223334445556667"]
        
        for card in valid_cards_to_test:
            self.assertTrue(isValidCard(card))

    def test_invalid_credit_card(self):
        """Here is a bunch of values I think should NOT work"""
        invalid_cards_to_test = ["111222333444", "11122233344455566677", "", " ", "1112223 334445"]
        
        for card in invalid_cards_to_test:
            self.assertFalse(isValidCard(card))
