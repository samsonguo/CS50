"""
Github Code

figlet = Figlet()
argv1 = ["-f", "--font"]

def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")


def figletize(prompt, f):
    txt = input(prompt)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(txt))


main()

"""


"""
Dior's Code 
import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    IsRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    IsRandomFont = False
else:
    sys.exit(1)

msg = input("Input: ")

figlet.getFonts()
if not IsRandomFont:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
"""

#My Code
import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

#Expects zero or two command-line arguments:

#Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())

 #Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f = sys.argv[2]

else:
    print("Invalid Usage")
    sys.exit(1)

#Prompts the user for a str of text.
user_input = input("Input: ")

#Outputs that text in the desired font.
figlet.setFont(font=f)
print(figlet.renderText(user_input))

