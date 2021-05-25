### On Windows machine:

You must have python set up in order to run the code. See https://www.python.org/downloads/ to find and install/download python.
Python 3.9 is recommended to run pygame faster. See https://phoenixnap.com/kb/how-to-install-python-3-windows on how to install python on Windows 

After python installation: 
install pygame: python -m pip install pygame, or pip install pygame
After pygame is set up, on terminal, please type: python game_interface.py

### On Mac machine:
The default python version is python 2.7.3. However, you can also download or install latest python version from: https://www.python.org/downloads/mac-osx/

On "Finder", select the project folder, locate to game_interface.py, right click on "Open With" and select "Python Launcher"
From Python Launcher, type: python game_interface.py (make sure pygame is installed, and the file is in current folder)

Second option: Note the project folder on Finder
               Hit command+space and type terminal, then hit enter.
               From terminal, type python game_interface.py (make sure it is in a current folder)

### Files:
- words.py: has a word property to store words from "3000english.txt" as a list
            A method to randomly choose a word from wordlist is expected to make sure that a random word at each play turn is selected and displayed. This will be helpful to build hangman.

- game_interface.py: Build a class that contain numerous properties to help set up pygame interface and visual/graphic design. Word property - a random word generated from a list of words - is needed and it inherited the word property from "Words" class in words.py 
                     Function outside this class calls game_interface methods to run the hangman game under main() 

- bignoodletoo.ttf: A file contains BigNoodleTooOblique font used to create text for buttons. On Windows machine, right click this file, select "install for all users" to make this text appear on the interface.

- hangman0-9.PNG: series of hangman images indicating the appearance process from a hanger to a hung person. Each hangman image will appear everytime the user/player guesses an incorrect letter