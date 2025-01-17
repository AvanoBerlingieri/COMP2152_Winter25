import random

print("Would you like to play?\n Enter 'yes' or 'no'")
play = input()
if play == 'no':
    print("maybe next time")
    quit()
correct = False
attempts = 0
targetNumber = random.randrange(1, 100)
print("guess the number between 1 and 10")
while correct == False:
    userInput = input("Enter your guess: ")
    if not userInput.isnumeric():
        print("Invalid input! Please enter a number between 1 and 100")
        continue
    if targetNumber == int(userInput):
        print("Congratulations! You've guessed it!")
        correct = True
        attempts += 1
    elif int(userInput) > targetNumber:
        print("Too high! Try again")
        correct = False
        attempts += 1
    else:
        print("Too low! Try again")
        correct = False
        attempts += 1
    if attempts == 10:
        print("Game over! The target number was [targetNumber].")
        break