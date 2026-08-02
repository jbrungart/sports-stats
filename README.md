# Tennis and Golf Athlete Information

## Description

This Python project displays information and statistics for professional tennis players and golfers. The program uses object-oriented programming to create athlete objects, simulate training and competitions, track tennis match results, and display athlete details. It also retrieves a player biography from theSportsDB website using web scraping.

## Features

* Creates and displays tennis player and golfer profiles
* Stores athlete information such as name, age, country, and professional year
* Simulates athlete training and competitions
* Tracks tennis sets won and determines match results
* Validates player equipment information
  * Tennis racquet grip size and head size
  * Golf club type and dominant hand
* Retrieves athlete information from a webpage using BeautifulSoup
* Includes unit tests to verify program functionality

## Files

* `main.py` - Driver file that creates athlete objects and demonstrates program features
* `athletes.py` - Contains the Athlete, TennisPlayer, and Golfer classes along with web scraping functionality
* `test_athletes.py` - Contains unit tests for validating class methods and attributes

## Requirements

* Python 3.x
* requests
* beautifulsoup4
* unittest

Install required packages with:

```bash
pip install requests beautifulsoup4
```

## How to Run

Run the main program:

```bash
python main.py
```

To run the unit tests:

```bash
python -m pytest test_athletes.py
```

## Object-Oriented Design

This project uses inheritance and abstraction:

* `Athlete` is an abstract base class containing shared athlete attributes.
* `Sport` is an abstract class defining training and competition behaviors.
* `TennisPlayer` and `Golfer` inherit from these classes and implement their own sport-specific features.

## Data Source

The project uses information from theSportsDB website to retrieve a description of a professional tennis player.

Rodgers , Aaron. “Welcome to TheSportsDB.Com.” TheSportsDB.Com- Free Sports API
Database with High Quality Artwork and Metadata, 2013, www.thesportsdb.com/.

## Authors

* Jade Brungart
* Violet Brungart
