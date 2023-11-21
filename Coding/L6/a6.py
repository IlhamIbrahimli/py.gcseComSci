# Task 1 - Guessing game 
# ----------------------
# Modify the program to count the number of guesses made by the user
# If they guess the word correctly within 10 guesses then give them a special treat.
guess = ""
word = "badger"
count = 0
print(f"I'm thinking of a word. It starts with '{word[0]}' and contains {len(word)} letters. ")
print("If you can guess it within 10 attempts you win a prize!")

while guess != word:
    guess = input("Enter your guess: ")
    if guess != word:
        print("Nope! Try again!")
    count += 1

print("You got it!")
if count <= 10:
    print("Good job here's a treat!")

# Task 2 - User authentication (login) system
# --------------------------------------------
# Modify this to allow up to three login attempts before being locked out.

username = ""
password = ""
valid_details = False
count = 0
print("Please login to continue..")

while valid_details == False:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "bob" and password == "letmein":
        valid_details = True
        print("You're in!")
    else:
        print("Incorrect details. Please try again.")
        count+=1

    if count == 3:
        print("You are locked out of the system.")
        break
    



# Task 3 - Character counter
# ---------------------------
# Write a program that asks the user to enter a string of text and counts the number of vowels it contains.
# Use a for loop to iterate through each character one-by-one, testing if it is a vowel and adding to a running
# total if it is.
inpStr = input("Enter text:")
vowelNum = 0
for i in inpStr:
    if i.lower() in ["a","e","i","o","u"]:
        vowelNum += 1

print(vowelNum)

# Task 4 - Menu-driven program
# -----------------------------
# Add a third menu option to perform a calculation (e.g. calculating the area of a triangle)
choice = ""

while choice != "Q":
    print("\n" * 20) # Clear the screen
    print("Choose an option from the menu:")
    print("--------------------------------")
    print("1. Tell me a joke")
    print("2. Sing me a song")
    print("3. Calculate area of a triangle")
    print("Q. Quit")
    print("--------------------------------")
    print()
    choice = input("> ").upper()

    if choice == "1":
        print("What's the best thing about Switzerland?")
        print()
        print("I don't know, but the flag is a big plus.")
        print()
        input("Press Enter to return to the menu...")

    elif choice == "2":
        print("""
        Blackbird (The Beatles)
        -----------------------

        Blackbird singing in the dead of night
        Take these broken wings and learn to fly
        All your life, you were only waiting
        For this moment to arise

        Blackbird singing in the dead of night
        Take these sunken eyes and learn to see
        All your life, you were only waiting
        For this moment to be free

        Blackbird fly
        Blackbird fly
        Into the light
        Of a dark, black night
        Blackbird fly
        Blackbird fly
        Into the light
        Of a dark, black night

        Blackbird singing in the dead of night
        Take these broken wings and learn to fly
        All your life, you were only waiting
        For this moment to arise

        """)

        input("Press Enter to return to the menu...")

    elif choice == "3":
        base = int(input("Enter base of triangle:"))
        height = int(input("Enter height of triangle"))
        area = (base*height)/2
        print(area)
        input("Press Enter to return to the menu...")

