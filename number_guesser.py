import random

# user input to delimitate the max number
user_input = input("Input a number: ")

# user input is a number
if user_input.isdigit():
  # if it is a number this line will convert it to a number and continue
  user_input = int(user_input)

# number has to be greater than 0 
  if user_input <= 0:
    print("Please insert a number greater than 0")
    quit()
else:
    print("Please only insert a number")
  

random_number = random.randint(0, user_input)
guesses = 0

while True:
  guesses += 1
  user_guess = input("Take a guess: ")
  if user_guess.isdigit(): 
    user_guess = int(user_guess)
  else:
    print("Please only insert a number")
    # will bring to the top of the loop
    continue

  if user_guess == random_number:
    print("You got it!")
    break
  elif user_guess > random_number:
      print("You were above the number!")
  else:
      print("You were below the number")

print("You got it in", guesses, "guesses")