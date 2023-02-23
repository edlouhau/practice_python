# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number = int(input("Enter a number: "))

remainder = number % 2

if remainder != 0:
    print("Your number is odd.")
else :
    print("Your number is even.")


