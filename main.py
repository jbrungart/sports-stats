"""A template for a python script deliverable for INST326.
Driver: Jade Brungart
Navigator: Violet Brungart
Assignment: Final Project
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

from athletes import Athlete, TennisPlayer, Golfer, fetch_paragraph_from_web


def main():
    
    """
    Main function that demonstrates the creation of TennisPlayer and Golfer objects, 
    simulates their actions (e.g., training, competing, and winning sets), 
    and displays updated information about them.

    Additionally, it fetches and prints data from the web about Paula Badosa.
    """
    
    # Example usage:
    try:
        # Creating Tennis Player
        tennis_player = TennisPlayer("Paula Badosa", 27, "Spain", 2015, 0, 0, "Red", 4.5, 100)
        print(tennis_player.display_info())
        print(tennis_player.train())
        print(tennis_player.compete())
        
        
        # Simulating winning sets
        tennis_player.win_set()  # Paula wins a set
        tennis_player.win_set()  # Paula wins another set


        # Display updated information
        print(tennis_player.display_info())


        # Check if Paula wins or loses the match
        print(tennis_player.check_match_result())
    
        # Using getters and setters
        tennis_player.grip_size = 4.8  # Updating grip size
        tennis_player.head_size = 120  # Updating head size
        print(tennis_player.display_info())  # Check updated info


        # Creating Golfer
        golfer = Golfer("Nelly Korda", 27, "USA", 2016, 0, 0, "driver", 45.5, "right")
        print(golfer.display_info())
        print(golfer.train())
        print(golfer.compete())

    
        # Using getters and setters
        golfer.club_type = "iron"  # Changing club type
        golfer.dominant_hand = "left"  # Changing dominant hand
        print(golfer.display_info())  # Check updated info


    except ValueError as e:
        print(e)
        
        
    ###############################################################################################################
    # Example of fetching data from the web
    url = 'https://www.thesportsdb.com/player/34203581-Paula-Badosa'
    paragraph_number = 1  
    paragraph_text = fetch_paragraph_from_web(url, paragraph_number)

    print("\n", paragraph_text)
    ###############################################################################################################


if __name__ == "__main__":
    main()

