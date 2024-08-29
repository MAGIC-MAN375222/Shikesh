# Simple Text-Based Adventure Game

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room. There are two doors in front of you.")
    print("Do you choose the left door or the right door?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        left_room()
    elif choice == 'right':
        right_room()
    else:
        print("Invalid choice. Please try again.")
        intro()

def left_room():
    print("You entered the left room. It's empty, except for a strange box.")
    print("Do you open the box or leave the room?")
    choice = input("Type 'open' or 'leave': ").lower()
    if choice == 'open':
        print("You open the box and find a treasure! You win!")
    elif choice == 'leave':
        print("You leave the room and return to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        left_room()

def right_room():
    print("You entered the right room. It's filled with monsters!")
    print("Do you fight or run?")
    choice = input("Type 'fight' or 'run': ").lower()
    if choice == 'fight':
        print("You fought bravely but lost. Game over.")
    elif choice == 'run':
        print("You ran away and returned to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        right_room()

# Start the game
intro()


# Adventure Game with Inventory and Puzzle Elements

# Player Inventory
inventory = []

# Introduction
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room. There are two doors in front of you.")
    print("Do you choose the left door or the right door?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        left_room()
    elif choice == 'right':
        right_room()
    else:
        print("Invalid choice. Please try again.")
        intro()

# Left Room - Includes a Puzzle
def left_room():
    print("\nYou entered the left room. It's empty, except for a strange box.")
    print("Do you open the box or leave the room?")
    choice = input("Type 'open' or 'leave': ").lower()
    
    if choice == 'open':
        if 'key' in inventory:
            print("You use the key to open the box and find a treasure! You win!")
        else:
            print("The box is locked. You need a key to open it.")
            left_room()  # Give player a chance to solve the puzzle by finding the key
    elif choice == 'leave':
        print("You leave the room and return to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        left_room()

# Right Room - Find the Key
def right_room():
    print("\nYou entered the right room. It's filled with strange symbols.")
    print("In the center of the room, there is a pedestal with a key on it.")
    print("Do you take the key or leave the room?")
    choice = input("Type 'take' or 'leave': ").lower()
    
    if choice == 'take':
        if 'key' in inventory:
            print("You already have the key.")
        else:
            print("You take the key and put it in your inventory.")
            inventory.append('key')
        print("You leave the room and return to the starting point.")
        intro()
    elif choice == 'leave':
        print("You leave the room and return to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        right_room()

# Start the game
intro()




import random

# Player attributes
inventory = []
health = 100
game_over = False

# Introduction
def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room. There are three doors in front of you.")
    print("Do you choose the left door, the center door, or the right door?")
    choice = input("Type 'left', 'center', or 'right': ").lower()
    
    if choice == 'left':
        left_room()
    elif choice == 'center':
        center_room()
    elif choice == 'right':
        right_room()
    else:
        print("Invalid choice. Please try again.")
        intro()

# Left Room - Contains a treasure but also a trap
def left_room():
    global health
    print("\nYou entered the left room. There is a shining treasure chest in the center.")
    print("Do you open the chest or leave the room?")
    
    choice = input("Type 'open' or 'leave': ").lower()
    
    if choice == 'open':
        if 'key' in inventory:
            print("You use the key to open the chest and find a pile of gold! You win!")
            print("Congratulations! You've completed the adventure with a fortune.")
            end_game()
        else:
            print("The chest was trapped! You lose 20 health.")
            health -= 20
            check_health()
            print("You leave the room and return to the starting point.")
            intro()
    elif choice == 'leave':
        print("You leave the room and return to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        left_room()

# Center Room - Combat with a monster
def center_room():
    print("\nYou entered the center room. A fierce monster stands before you!")
    print("Do you fight the monster or run away?")
    
    choice = input("Type 'fight' or 'run': ").lower()
    
    if choice == 'fight':
        combat()
    elif choice == 'run':
        print("You manage to escape and return to the starting point.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        center_room()

# Combat System
def combat():
    global health
    monster_health = 50
    print("\nThe battle begins!")
    
    while monster_health > 0 and health > 0:
        attack = random.randint(10, 30)
        monster_attack = random.randint(5, 15)
        
        print(f"You attack the monster and deal {attack} damage!")
        monster_health -= attack
        
        if monster_health > 0:
            print(f"The monster attacks and deals {monster_attack} damage!")
            health -= monster_attack
            check_health()
        else:
            print("You defeated the monster!")
            inventory.append('key')  # Reward: key for the treasure
            print("You find a key on the monster. It may be useful later.")
            intro()

# Ri
