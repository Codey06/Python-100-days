# # Assigning an integer value to a variable
# # my_int = 10

# # # Assigning a floating-point value to a variable
# # my_float = 20.5

# # # Assigning a string value to a variable
# # my_string = "Hello, World!"

# # # Assigning a boolean value to a variable
# # my_bool = True

# # # Variables
# # name=input("Whats your name")
# # print(name)
# # print(len(input("What is your name ")))

# # Assigning values to variables
# num1 = input()
# num2 = input()

# # Performing arithmetic operations using variables
# sum_result = num1 + num2
# difference_result = num1 - num2
# product_result = num1 * num2
# division_result = num1 / num2

# # Printing the results
# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Division:", division_result)







# Gaming

# import random

# def number_guessing_game():
#     # Generate a random number between 1 and 100
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#     guessed_correctly = False

#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")

#     while not guessed_correctly:
#         # Get the player's guess
#         try:
#             guess = int(input("Take a guess: "))
#             attempts += 1

#             # Check if the guess is correct
#             if guess < number_to_guess:
#                 print("Your guess is too low.")
#             elif guess > number_to_guess:
#                 print("Your guess is too high.")
#             else:
#                 guessed_correctly = True
#                 print(f"Congratulations! You guessed the number in {attempts} attempts.")
#         except ValueError:
#             print("Please enter a valid number.")

# # Run the game
# number_guessing_game()
