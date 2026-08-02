"""A template for a python script deliverable for INST326.
Driver: Jade Brungart
Navigator: Violet Brungart
Assignment: Final Project unit tests
Date: 12_13_24
"""

import requests
from abc import ABC, abstractmethod
from argparse import ArgumentParser
import argparse
import sys
import random
import string   
string.ascii_letters
from bs4 import BeautifulSoup

import unittest
from athletes import TennisPlayer, Golfer

class TestTennisPlayer(unittest.TestCase):
    """
    Unit tests for the TennisPlayer class.

    This class contains tests for verifying the functionality of the TennisPlayer class methods, 
    such as initialization, set wins, set losses, match result checking, and grip size validation.
    """

    def test_initialization(self):
        """
        Test that TennisPlayer is initialized with correct attributes.

        This test checks whether the TennisPlayer object is initialized correctly with the expected 
        name, age, team, racquet color, grip size, and head size.
        """
        # Test if the TennisPlayer is initialized correctly
        player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        self.assertEqual(player.name, "Paula Badosa")
        self.assertEqual(player.age, 27)
        self.assertEqual(player.team, "Spain")
        self.assertEqual(player.racquet_color, "Red")
        self.assertEqual(player.grip_size, 4.5)
        self.assertEqual(player.head_size, 100)

    def test_invalid_grip_size(self):
        """
        Test invalid grip size input raises ValueError.

        This test ensures that if the grip size is outside the valid range (4.0 to 5.0), 
        a ValueError is raised during initialization.
        """
        # Test invalid grip size (should raise ValueError)
        with self.assertRaises(ValueError):
            TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 3.5, 100)

    def test_win_set(self):
        """
        Test the win_set method increments sets_won correctly.

        This test verifies that the `win_set` method correctly increments the sets_won attribute 
        when a set is won by the player.
        """
        # Test the win_set method
        player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        player.win_set()
        self.assertEqual(player.sets_won, 1)

    def test_lose_set(self):
        """
        Test the lose_set method decrements sets_won correctly.

        This test checks that the `lose_set` method correctly decreases the sets_won attribute 
        when a set is lost, while ensuring that the sets_won value doesn't drop below 0.
        """
        # Test the lose_set method
        player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        player.win_set()
        player.lose_set()
        self.assertEqual(player.sets_won, 0)

    def test_check_match_result_win(self):
        """
        Test the check_match_result method identifies a win correctly.

        This test verifies that the `check_match_result` method returns the correct result 
        when the player wins the match (at least 2 sets won).
        """
        # Test if the check_match_result method correctly identifies a win
        player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        player.win_set()
        player.win_set()
        result = player.check_match_result()
        self.assertEqual(result, "Paula Badosa wins the match with 2 sets.")

    def test_check_match_result_loss(self):
        """
        Test the check_match_result method identifies a loss correctly.

        This test ensures that the `check_match_result` method correctly returns the result 
        when the player loses the match (less than 2 sets won).
        """
        # Test if the check_match_result method correctly identifies a loss
        player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        player.win_set()
        result = player.check_match_result()
        self.assertEqual(result, "Paula Badosa loses the match with only 1 sets.")


class TestGolfer(unittest.TestCase):
    """
    Unit tests for the Golfer class.

    This class contains tests for verifying the functionality of the Golfer class methods, 
    such as initialization, club type validation, dominant hand validation, and the display_info method.
    """
    def test_initialization(self):
        """
        Test that Golfer is initialized with correct attributes.

        This test verifies that the Golfer object is correctly initialized with the expected 
        name, team, club type, and dominant hand.
        """
        # Test if the Golfer is initialized correctly
        golfer = Golfer("Nelly Korda", 27, "USA", 2016, 0, 0, "driver", 45.5, "right")
        self.assertEqual(golfer.name, "Nelly Korda")
        self.assertEqual(golfer.team, "USA")
        self.assertEqual(golfer.club_type, "driver")
        self.assertEqual(golfer.dominant_hand, "right")

    def test_invalid_club_type(self):
        """
        Test invalid club type input raises ValueError.

        This test ensures that an invalid club type (not one of 'driver', 'iron', 'putter') 
        raises a ValueError when initializing the Golfer object.
        """
        # Test invalid club type (should raise ValueError)
        with self.assertRaises(ValueError):
            Golfer("Nelly Korda", 27, "USA", 2016, 0, 0, "invalid_club", 45.5, "right")

    def test_invalid_dominant_hand(self):
        """
        Test invalid dominant hand input raises ValueError.

        This test checks that if the dominant hand is not either 'left' or 'right', 
        a ValueError is raised during initialization.
        """
        # Test invalid dominant hand (should raise ValueError)
        with self.assertRaises(ValueError):
            Golfer("Nelly Korda", 27, "USA", 2016, 0, 0, "driver", 45.5, "center")

    def test_display_info(self):
        """
        Test the display_info method for correct information.

        This test verifies that the `display_info` method returns a string with the correct 
        information about the Golfer, including the name, club type, and shaft length.
        """
        # Test the display_info method
        golfer = Golfer("Nelly Korda", 27, "USA", 2016, 0, 0, "driver", 45.5, "right")
        info = golfer.display_info()
        self.assertIn("Golfer Nelly Korda", info)
        self.assertIn("Club Type: driver", info)
        self.assertIn("Shaft Length: 45.5", info)


if __name__ == "__main__":
    unittest.main()


# note to self
#python -m pytest test_athletes.py