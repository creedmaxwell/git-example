import random

print("Hello! This program is going to try and guess your age.\n")
name = input("What is your name: ")
age = 0
correct = False

guesses = []

while (correct == False):
    age = random.randint(15,30)
    if age in guesses:
        continue
    guess = input("\nIs this your age: " + str(age))
    if guess == "y":
        correct = True
    else:
        print("Rats.")
        guesses.append(age)

print(name + " is " + str(age) + " years old.")

