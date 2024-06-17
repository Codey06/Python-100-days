# 1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their cursor showss on a new line:

#5. make sure the input cursor shows on a new line:

# print("hey Welcome back 😂")
# city=input("What is the city you Grow Up ! \n")
# name=input("Please tell us your name\n")
# print("Your name is \n "+name+ "And your Grow Up \n "+city)
def main():
    # 1. Create a greeting for your program.
    print("Welcome to the Band Name Generator!")

    # 2. Ask the user for the city that they grew up in.
    city = input("What's the name of the city you grew up in?\n")

    # 3. Ask the user for the name of a pet.
    pet = input("What's your pet's name?\n")

    # 4. Combine the name of their city and pet and show them their band name.
    band_name = city + " " + pet
    print("Your band name could be: " + band_name)

# Run the program
main()
