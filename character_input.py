# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
turns_100 = 100 - age + 2023

print(f"You will turn a 100 years old by te year {turns_100}.")


