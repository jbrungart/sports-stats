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


# Abstract parent class for Athlete
class Athlete(ABC):
    """
    Abstract base class for representing an athlete. This class provides the basic 
    attributes and getter/setter methods for an athlete, such as name, age, team, 
    year they turned professional, and their position on a field (represented by 
    x and y coordinates).
    
    Subclasses must implement the display_info() method.
    """
    def __init__(self, name, age, team, year_turned_pro, x_position, y_position):
        
        """
        Initialize an Athlete instance with basic attributes.
        
        Args:
            name (str): The name of the athlete.
            age (int): The age of the athlete.
            team (str): The team the athlete belongs to.
            year_turned_pro (int): The year the athlete turned professional.
            x_position (float): The x-coordinate of the athlete's position.
            y_position (float): The y-coordinate of the athlete's position.
        """
        self._name = name
        self._age = age
        self._team = team
        self._year_turned_pro = year_turned_pro
        self._x_position = x_position
        self._y_position = y_position


    # Getters and Setters
    @property
    def name(self):
        """
        Get the name of the athlete.
        
        Returns:
            str: The name of the athlete.
        """
        return self._name


    @name.setter
    def name(self, name):
        """
        Set the name of the athlete.
        
        Args:
            name (str): The new name of the athlete.
        """
        self._name = name


    @property
    def age(self):
        """
        Get the age of the athlete.
        
        Returns:
            int: The age of the athlete.
        """
        return self._age


    @age.setter
    def age(self, age):
        """
        Set the age of the athlete.
        
        Args:
            age (int): The new age of the athlete.
        """
        self._age = age


    @property
    def team(self):
        """
        Get the team of the athlete.
        
        Returns:
            str: The team the athlete belongs to.
        """
        return self._team


    @team.setter
    def team(self, team):
        """
        Set the team of the athlete.
        
        Args:
            team (str): The new team the athlete belongs to.
        """
        self._team = team


    @property
    def year_turned_pro(self):
        """
        Get the year the athlete turned professional.
        
        Returns:
            int: The year the athlete turned professional.
        """
        return self._year_turned_pro


    @year_turned_pro.setter
    def year_turned_pro(self, year_turned_pro):
        """
        Set the year the athlete turned professional.
        
        Args:
            year_turned_pro (int): The year the athlete turned professional.
        """
        self._year_turned_pro = year_turned_pro


    @property
    def x_position(self):
        """
        Get the x-coordinate of the athlete's position.
        
        Returns:
            float: The x-coordinate of the athlete's position.
        """
        return self._x_position


    @x_position.setter
    def x_position(self, x_position):
        """
        Set the x-coordinate of the athlete's position.
        
        Args:
            x_position (float): The new x-coordinate of the athlete's position.
        """
        self._x_position = x_position


    @property
    def y_position(self):
        """
        Get the y-coordinate of the athlete's position.
        
        Returns:
            float: The y-coordinate of the athlete's position.
        """
        return self._y_position


    @y_position.setter
    def y_position(self, y_position):
        """
        Set the y-coordinate of the athlete's position.
        
        Args:
            y_position (float): The new y-coordinate of the athlete's position.
        """
        self._y_position = y_position


    @abstractmethod
    def display_info(self):
        """
        Abstract method to display the athlete's information.
        
        This method must be implemented by any subclass of Athlete to display 
        relevant information about the athlete.
        """
        pass


# Abstract parent class for Sport
class Sport(ABC):
    """
    Abstract base class for representing a sport. Subclasses of Sport must implement 
    the train and compete methods to define the specific actions related to training 
    and competing in that sport.
    """
    @abstractmethod
    def train(self):
        """
        Abstract method to simulate training for the sport.
        
        Subclasses must implement this method to define the specific training process.
        """
        pass
   
    @abstractmethod
    def compete(self):
        """
        Abstract method to simulate competing in the sport.
        
        Subclasses must implement this method to define the competition process.
        """
        pass


# Child class TennisPlayer
class TennisPlayer(Athlete, Sport):
    """
    A class representing a Tennis Player, inheriting from Athlete and Sport. 
    This class includes specific attributes and methods related to tennis players, 
    such as racquet color, grip size, head size, and the number of sets won.
    
    Methods for winning and losing sets, along with appropriate validation for grip size 
    and head size, are also included.
    """
    def __init__(self, name, age, team, year_turned_pro, x_position, y_position, racquet_color, grip_size, head_size):
        """
        Initialize a TennisPlayer instance with specific attributes for a tennis player.
        
        Args:
            name (str): The name of the tennis player.
            age (int): The age of the tennis player.
            team (str): The team the player belongs to (if applicable).
            year_turned_pro (int): The year the player turned professional.
            x_position (float): The x-coordinate of the player's position on the court.
            y_position (float): The y-coordinate of the player's position on the court.
            racquet_color (str): The color of the player's racquet.
            grip_size (float): The grip size of the player's racquet, between 4.0 and 5.0 inches.
            head_size (float): The head size of the player's racquet, between 85 and 135 square inches.
        
        Raises:
            ValueError: If grip size or head size are out of the valid range.
        """
        # Initialize the parent classes
        Athlete.__init__(self, name, age, team, year_turned_pro, x_position, y_position)
        self._racquet_color = racquet_color
        self._grip_size = grip_size
        self._head_size = head_size
        self._sets_won = 0


        # Validate grip size and head size
        if not (4.0 <= grip_size <= 5.0):
            raise ValueError("Grip size must be between 4.0 and 5.0 inches.")
        if not (85 <= head_size <= 135):
            raise ValueError("Head size must be between 85 and 135 square inches.")


    # Getters and Setters for TennisPlayer specific attributes
    @property
    def racquet_color(self):
        """
        Get the color of the tennis player's racquet.
        
        Returns:
            str: The color of the racquet.
        """
        return self._racquet_color


    @racquet_color.setter
    def racquet_color(self, racquet_color):
        """
        Set the color of the tennis player's racquet.
        
        Args:
            racquet_color (str): The new color of the racquet.
        """
        self._racquet_color = racquet_color


    @property
    def grip_size(self):
        """
        Get the grip size of the tennis player's racquet.
        
        Returns:
            float: The grip size of the racquet.
        """
        return self._grip_size


    @grip_size.setter
    def grip_size(self, grip_size):
        """
        Set the grip size of the tennis player's racquet.
        
        Args:
            grip_size (float): The new grip size of the racquet, must be between 4.0 and 5.0 inches.
        
        Raises:
            ValueError: If the grip size is not in the valid range.
        """
        if not (4.0 <= grip_size <= 5.0):
            raise ValueError("Grip size must be between 4.0 and 5.0 inches.")
        self._grip_size = grip_size


    @property
    def head_size(self):
        """
        Get the head size of the tennis player's racquet.
        
        Returns:
            float: The head size of the racquet in square inches.
        """
        return self._head_size


    @head_size.setter
    def head_size(self, head_size):
        """
        Set the head size of the tennis player's racquet.
        
        Args:
            head_size (float): The new head size of the racquet, must be between 85 and 135 square inches.
        
        Raises:
            ValueError: If the head size is not in the valid range.
        """
        if not (85 <= head_size <= 135):
            raise ValueError("Head size must be between 85 and 135 square inches.")
        self._head_size = head_size
        
    @property
    def sets_won(self):
        """
        get the number of sets won by the tennis player.
        
        Args:
            sets_won (int): The number of sets won by the player.
        """
        return self._sets_won


    @sets_won.setter
    def sets_won(self, sets_won):
        """
        Set the number of sets won by the tennis player.
        
        Args:
            sets_won (int): The number of sets won by the player.
        """
        self._sets_won = sets_won
        
    
    def win_set(self):
        """
        Increment the number of sets won by the player.
        
        This method is called when the player wins a set. The `sets_won` attribute is 
        increased by 1.
        """
        self._sets_won += 1
    
    
    def lose_set(self):
        """
        Decrement the number of sets won by the player.
        
        This method is called when the player loses a set. The `sets_won` attribute is 
        decreased by 1, unless the player has already won 0 sets, in which case it raises 
        a ValueError.
        
        Raises:
            ValueError: If the player has not won any sets and cannot lose more sets.
        """
        if self._sets_won >0:
            self._sets_won -= 1
        else:
            raise ValueError("Cannot lose more sets. The score is already at 0.")


    # New method to check if the player has won the match
    def check_match_result(self):
        """
    Check the result of the tennis match based on the number of sets won.
    
    This method determines whether the player has won or lost the match based 
    on the number of sets they've won. A player needs to win at least 2 sets 
    to be considered a winner.
    
    Returns:
        str: A message indicating whether the player wins or loses the match, 
             including the number of sets won.
         """

        if self._sets_won >= 2:
            return f"{self.name} wins the match with {self._sets_won} sets."
        else:
            return f"{self.name} loses the match with only {self._sets_won} sets."

        

    def display_info(self):
        """
    Display detailed information about the tennis player.
    
    This method returns a string containing various details about the player, 
    including their name, age, team/country, professional status, position, 
    and racquet specifications.
    
    Returns:
        str: A formatted string with the player's information.
    """
        return f"Tennis Player {self.name}, Age: {self.age}, Team/Country: {self.team}, " \
               f"Pro Since: {self.year_turned_pro}, Position: ({self.x_position}, {self.y_position}), " \
               f"Racquet Color: {self.racquet_color}, Grip Size: {self.grip_size}, Head Size: {self.head_size}"


    def train(self):
        """
    Simulate the tennis player's training session.
    
    This method returns a message indicating that the player is training on 
    the tennis court.
    
    Returns:
        str: A message indicating that the player is training.
    """
        return f"{self.name} is training on the tennis court."


    def compete(self):
        """
    Simulate the tennis player's competition in a match.
    
    This method returns a message indicating that the player is competing in 
    a tennis match.
    
    Returns:
        str: A message indicating that the player is competing in a match.
    """
        return f"{self.name} is competing in a tennis match."


# Child class Golfer
class Golfer(Athlete, Sport):
    """
    A class representing a Golfer, inheriting from Athlete and Sport. 
    This class includes specific attributes and methods related to golfers, 
    such as club type, shaft length, and dominant hand, as well as methods 
    for displaying information, training, and competing.
    """
    def __init__(self, name, age, team, year_turned_pro, x_position, y_position, club_type, shaft_length, dominant_hand):
        """
        Initialize a Golfer instance with specific attributes for a golfer.
        
        Args:
            name (str): The name of the golfer.
            age (int): The age of the golfer.
            team (str): The team or country the golfer belongs to.
            year_turned_pro (int): The year the golfer turned professional.
            x_position (float): The x-coordinate of the golfer's position.
            y_position (float): The y-coordinate of the golfer's position.
            club_type (str): The type of club the golfer uses (driver, iron, putter).
            shaft_length (float): The length of the golf club's shaft.
            dominant_hand (str): The dominant hand of the golfer, either "left" or "right".
        
        Raises:
            ValueError: If the club type is invalid or the dominant hand is not 'left' or 'right'.
        """
        # Initialize the parent classes
        Athlete.__init__(self, name, age, team, year_turned_pro, x_position, y_position)
        self._club_type = club_type
        self._shaft_length = shaft_length
        self._dominant_hand = dominant_hand


        # Validate club type and dominant hand
        valid_club_types = ["driver", "iron", "putter"]
        if self.club_type not in valid_club_types:
            raise ValueError(f"Invalid club type. Must be one of {valid_club_types}.")
       
        if self.dominant_hand not in ["left", "right"]:
            raise ValueError("Dominant hand must be 'left' or 'right'.")


    # Getters and Setters for Golfer specific attributes
    @property
    def club_type(self):
        """
        Get the type of club the golfer uses.
        
        Returns:
            str: The type of golf club (driver, iron, or putter).
        """
        return self._club_type


    @club_type.setter
    def club_type(self, club_type):
        """
        Set the type of club the golfer uses.
        
        Args:
            club_type (str): The type of golf club (driver, iron, or putter).
        
        Raises:
            ValueError: If the club type is not valid.
        """
        valid_club_types = ["driver", "iron", "putter"]
        if club_type not in valid_club_types:
            raise ValueError(f"Invalid club type. Must be one of {valid_club_types}.")
        self._club_type = club_type


    @property
    def shaft_length(self):
        """
        Get the length of the golf club's shaft.
        
        Returns:
            float: The length of the shaft in inches.
        """
        return self._shaft_length


    @shaft_length.setter
    def shaft_length(self, shaft_length):
        """
        Set the length of the golf club's shaft.
        
        Args:
            shaft_length (float): The length of the shaft in inches.
        """
        self._shaft_length = shaft_length


    @property
    def dominant_hand(self):
        """
        Get the dominant hand of the golfer.
        
        Returns:
            str: The dominant hand of the golfer ('left' or 'right').
        """
        return self._dominant_hand


    @dominant_hand.setter
    def dominant_hand(self, dominant_hand):
        """
        Get the dominant hand of the golfer.
        
        Returns:
            str: The dominant hand of the golfer ('left' or 'right').
        """
        if dominant_hand not in ["left", "right"]:
            raise ValueError("Dominant hand must be 'left' or 'right'.")
        self._dominant_hand = dominant_hand


    def display_info(self):
        """
        Display detailed information about the golfer.
        
        This method returns a string containing various details about the golfer, 
        including their name, age, team/country, professional status, position, 
        and golf club specifications.
        
        Returns:
            str: A formatted string with the golfer's information.
        """
        return f"Golfer {self.name}, Age: {self.age}, Team/Country: {self.team}, " \
               f"Pro Since: {self.year_turned_pro}, Position: ({self.x_position}, {self.y_position}), " \
               f"Club Type: {self.club_type}, Shaft Length: {self.shaft_length}, Dominant Hand: {self.dominant_hand}"


    def train(self):
        """
        Simulate the golfer's training session.
        
        This method returns a message indicating that the golfer is training on 
        the golf course.
        
        Returns:
            str: A message indicating that the golfer is training.
        """
        return f"{self.name} is training on the golf course."


    def compete(self):
        """
        Simulate the golfer's competition in a tournament.
        
        This method returns a message indicating that the golfer is competing in 
        a golf tournament.
        
        Returns:
            str: A message indicating that the golfer is competing in a tournament.
        """
        return f"{self.name} is competing in a golf tournament."

###############################################################################################################
# Function to fetch data from a URL and extract a specific paragraph
def fetch_paragraph_from_web(url, paragraph_number):
    """
    Fetch a specific paragraph from a web page given a URL and paragraph number.
    
    This function retrieves the HTML content from the provided URL and extracts 
    the text from a specified paragraph number. If the paragraph number is 
    out of range, it returns an error message.
    
    Args:
        url (str): The URL of the webpage to fetch content from.
        paragraph_number (int): The paragraph number to extract, 1-based index.
    
    Returns:
        str: The text of the specified paragraph or an error message if the paragraph is not found.
    """
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all paragraphs
            paragraphs = soup.find_all('p')
            
            # Check if the paragraph number exists in the list
            if paragraph_number <= len(paragraphs):
                return paragraphs[paragraph_number - 1].get_text()  # Get the text of the specified paragraph
            else:
                return f"Paragraph {paragraph_number} not found."
        else:
            return f"Error: Unable to fetch the URL. Status code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
###############################################################################################################
