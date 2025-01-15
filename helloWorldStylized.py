# A simple program that takes the username (provided by you) and prints a greeting. 
# NOTE: You might have to install pyfiglet before execution. Pyfiglet LINK: https://github.com/pwaller/pyfiglet 
# Pyfiglet author: pwaller
# Install command: pip install pyfiglet

import pyfiglet
from pyfiglet import Figlet

f = Figlet(font = "electronic")

name = input ("Hello, please type your name: ")
greetings = "Hello"
print(f.renderText(greetings + " " + name + ", it's a great day for coding : )"))