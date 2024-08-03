import random

# r = random.randrange(0, 11)

top_of_range = input("Type a number: ")

# we need to check if they type a number...

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # if its not bigger than 0...
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()

# if its not a digit
else:
    print("Please type a number next time.")
    quit()

# we create the number
random_number = random.randint(0, top_of_range)

# initialize the guesses
guesses = 0

# we have to break out of the loop if the user gets it right
while True:
    guesses += 1
    # we ask for their answer
    user_guess = input("Take a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please time a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You are below the number.")

print("You got it in", guesses, "guesses")