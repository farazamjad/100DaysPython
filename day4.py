#ROCK PAPER SCISSOR GAME USING RANDOM LIBRARY

#----------------------------------------------------------------SHAPES--------------------------------------------------------------------------------------------------------------------------------
# Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
#importing random library
import random
print("Welcome to Rock, Paper and Scissors game!\n")
name=input("Enter your name: ")
player=int(input(("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")))
if player == 0:
    print(f"{name.upper()} Chose Rock")
    print(rock)
elif player ==1:
    print(f"{name.upper()} Chose Paper")
    print(paper)
elif player==2:
    print(f"{name.upper()} Chose Scissors")
    print(scissors)
else:
    print("Invalid player")    

#computer turn using random
computer=random.randint(0,2)
if computer == 0:
    print("Computer Chose Rock")
    print(rock)
elif computer ==1:
    print("Computer Chose Paper")
    print(paper)
elif computer==2:
    print("Computer Chose Scissors")
    print(scissors)
 
 #game rules
if player == computer:
  print("It's a tie!")
elif player == 0:
  if computer == 2:
    print("Rock smashes scissors! You win!")
  else:
    print("Paper covers rock! You lose.")
elif player == 1:
  if computer == 0:
    print("Paper covers rock! You win!")
  else:
    print("Scissors cuts paper! You lose.")
elif player == 2:
  if computer == 1:
    print("Scissors cuts paper! You win!")
  else:
    print("Rock smashes scissors! You lose.")

