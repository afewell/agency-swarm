import os
import sys
import time

# GameState to keep track of player's progress
class GameState:
    def __init__(self):
        self.clues = []
        self.arrest_made = False

    def add_clue(self, clue):
        self.clues.append(clue)

    def make_arrest(self):
        self.arrest_made = True

# Game state variable
state = GameState()

# Function to clear the screen

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function that starts the game

def begin_game():
    clear_screen()
    print('Welcome to the Mystery Detective Game!')
    time.sleep(2)
    introduction()

# Introduction to the game

def introduction():
    clear_screen()
    print("As the city's most esteemed detective, you're tasked with catching The Phantom.")
    time.sleep(2)
    start_investigation()

# Starting the investigation

def start_investigation():
    clear_screen()
    print("The Grand Museum's rare gem has been stolen, and you arrive at the crime scene.")
    time.sleep(2)
    player_choice()

# Player choice

def player_choice():
    print('\nWhat will you do?')
    print('1. Inspect the broken display case.')
    print('2. Interview the security guard.')
    print('3. Check surveillance footage.')
    choice = input('> ')
    handle_choice(choice)

# Handle player's choice

def handle_choice(choice):
    if choice == '1':
        inspect_case()
    elif choice == '2':
        interview_guard()
    elif choice == '3':
        check_footage()
    else:
        print('Invalid choice. Please select 1, 2, or 3.')
        player_choice()

# Inspect the broken display case

def inspect_case():
    print('\nYou notice a strange symbol etched near the lock.')
    state.add_clue('Symbol near the lock')
    if 'Security guard testimony' in state.clues:
        make_conclusion()
    else:
        player_choice()

# Interview the security guard

def interview_guard():
    print('\nThe guard recalls seeing a figure tampering with the lock just before the alarm.')
    state.add_clue('Security guard testimony')
    if 'Symbol near the lock' in state.clues:
        make_conclusion()
    else:
        player_choice()

# Check surveillance footage

def check_footage():
    print('\nYou discover that the surveillance cameras were disabled at a very specific time.')
    state.add_clue('Disabled cameras')
    player_choice()

# Make a conclusion and resolve the game

def make_conclusion():
    print('\nThe evidence is clear...')
    time.sleep(2)
    if len(state.clues) >= 2:
        print('You gather the police and arrest the suspect hiding in the museum!')
        state.make_arrest()
    else:
        print('There is not enough evidence to make an arrest. The Phantom eludes you once more...')

    print('\nGame Over!')
    sys.exit()

# Main game loop
if __name__ == '__main__':
    begin_game()
