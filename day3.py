
print('''

                            *************************
                            * Treasure Hunt Game! *
                            *************************



*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************


''')

print("Welcome to Treasure Island!\n")
print("Your mission is to find the hidden treasure chest!!!\n")

name = input("Enter your Name: ")
print(f"Welcome {name.upper()}, to the daring adventure of the Treasure Island.\n")

first = input("Move 1: As you step onto the island, do you choose to go Left or Right:\n")

if first.lower() == 'right':
    print("Oops, you've accidentally fallen off a cliff! Game Over!\n")
else:
    print("\nMove 2: A river blocks your path. Would you like to swim across or wait for a boat?\n")
    second = input("Enter Swim or Wait:\n")

    if second.lower() == 'swim':
        print('\nOh no! You are ambushed by a school of sharks. Game Over!\n')
    else:
        print("Lucky you! A magical boat appears out of thin air and takes you to the other side of the river.")
        print("The boat drops you in front of a mysterious cave with three doors.")
        print("You step inside the cave and see three doors ahead of you:\n")
        print("1. A Red door with strange engravings.")
        print("2. A Blue door that seems to shimmer faintly.")
        print("3. A Yellow door with a faint, warm glow.")

        third = int(input("\nMove 3: Choose wisely, enter the number of the door you want to open:\n"))

        if third == 1:
            print("\nAs the red door creaks open, you're caught in a pitfall trap! Game Over!\n")
        elif third == 2:
            print("\nOops! The blue door was a cleverly disguised illusion. A trapdoor opens beneath your feet! Game Over!\n")
        elif third == 3:
            print("\nCongratulations, adventurer! You've found the treasure chest and are now rich beyond your wildest dreams!\n")
        else:
            print("Oops, you've made an invalid choice. The doors vanish, and you're trapped forever. Game Over!\n")

print("\nThanks for playing!")



