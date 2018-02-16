import sys
import os
from random import randint, shuffle

menuHint = "You may type menu at any time."

level1Passwords = ["books", "aisle", "shelf", "password", "font", "borrow"]
level2Passwords = ["prisoner", "handcuffs", "holster", "uniform", "arrest"]
level3Passwords = ["starfield", "telescope", "environment", "exploration", "astronauts"]

currentScreen = None

def ShowMainMenu():
    global currentScreen
    currentScreen = "MainMenu"
    os.system('cls')
    print("What would you like to hack into?")
    print("Press 1 for the local library")
    print("Press 2 for the police station")
    print("Press 3 for NASA!")
    print("Enter your selection:")


def OnUsertext(text):
    if (text == "menu"): # we can always go direct to main menu
        ShowMainMenu()
    elif (text == "quit" or text == "close" or text == "exit"):
        sys.exit()
    elif (currentScreen == "MainMenu"):
        RunMainMenu(text)
    elif (currentScreen == "Password"):
        CheckPassword(text)


def RunMainMenu(text):
    isValidLevelNumber = (text == "1" or text == "2" or text == "3")
    if (isValidLevelNumber):
        global level
        level = int(text)
        AskForPassword()
    elif (text == "007"): # easter egg
        print("Please select a level Mr Bond!")
    else:
        print("Please choose a valid level")
        print(menuHint)
        

def AskForPassword():
    global currentScreen
    currentScreen = "Password"
    os.system('cls')
    SetRandomPassword()
    print("Enter your password, hint: " + Anagram(password))
    print(menuHint)

def Anagram(password):
    password = list(password)
    shuffle(password)
    return ''.join(password)

    
def SetRandomPassword():
    global password
    if (level == 1):
        password = level1Passwords[randint(0, len(level1Passwords)) - 1]
    elif (level == 2):
        password = level2Passwords[randint(0, len(level2Passwords)) - 1]
    elif (level == 3):
        password = level3Passwords[randint(0, len(level3Passwords)) - 1]
    else:
        print("Invalid level number")


def CheckPassword(text):
    if (text == password):
        DisplayWinScreen()
    else:
        AskForPassword()
        

def DisplayWinScreen():
    global currentScreens
    currentScreen = "Win"
    os.system('cls')
    ShowLevelReward()
    print(menuHint)
    

def ShowLevelReward():
    if (level == 1):
        print("Have a book...")
        print("""
                _______
               /      //
              /      //
             /_____ //
            (______(/           

        """)

    elif (level == 2):
        print("You got the prison key!")
        print("Play again for a greater challenge.")
        print("""
             __
            /0 \_______
            \__/-=' = '         

        """)
            
    elif (level == 3):
        print("""
         _ __   __ _ ___  __ _
        | '_ \ / _` / __|/ _` |
        | | | | (_| \__ \ (_| |
        |_| |_|\__,_|___)\__,_|

        """)
        print("Welcome to NASA's internal system!")

    else:
        print("Invalid level reached")

# Use this for initialization
ShowMainMenu()
while True:
    OnUsertext(input())
