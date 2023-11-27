import random

secret = random.randint(0, 10)
guess_count = 0
guess_limit = 3
print("Guess number between 0 to 10 (You have 3 tries)")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret:
        print("You won! ")
        break
    else:
        print("Wrong choice, try again")
else:
    print(f"Sorry you failed!! Guess number was {secret}")
