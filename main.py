import random
import sys

    

print("Welcome Numburdles! Guess the three digit number!")
   
def number_generator():
  """ Generates 3 digit number"""
  global numbers3
  numbers = random.randint(100,999)
  numbers2 = str(numbers)
  numbers3 = [int(x) for x in numbers2]  

def stop_game():
  """Stops Game""" 
  global y
  start= input("Game has ended do you want to play again y/n? ")
  
  if start == 'y':
   print("Ok lets start again!")
   number_generator()
   print(numbers3)
   start_game()
  elif start == 'n':
    y=2
    print("Game Over!")
  else:
    print("This input is not valid")
    stop_game()

def clues():
  """ Clues for guess""" 
  if numbers3 == x:
    print("you win!")
    stop_game()
    y=2
  elif numbers3[0] and x[0] == numbers3[1] and x[1] or numbers3[1] and x[1] == numbers3[1] and x[2] or numbers3[0] and x[0] == numbers3[2] and x[2]:
    print("You guess more than one correct!")   
  elif numbers3[0] == x[0]:
    print("You have a match, try again!")
  elif numbers3[1] == x[1]:
    print("You have a match, try again!")
  elif numbers3[2] == x[2]:
    print("You have a match, try again!")
  
  else:
    print("No match, try again!")

def start_game():
  global x
  global y
  y=0
  while y != 2:
    player2 = input("What is your guess?: ")
    if player2 > "999" or player2 < "111":
      print("This input is not valid")
    else:
      try:
        x = [int(x) for x in player2]
        clues()
      except ValueError:
        print("This input is not valid") 
      
number_generator()
print(numbers3)
start_game()



#or numbers3[1,2] == x[1,2] or numbers3[0,2] == x[0,2]:

  
# for x in range(7):
#   if x == 6:
#     print("You're out of guesses!")
#     stop_game()
#   player2 = input("What is your guess?: ")
#   try:
#     x = [int(x) for x in player2]
#     clues()
#   except ValueError:
#     print("This input is not valid")
