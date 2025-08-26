import random


def main():
    print("I'm going to guess your age!")
    name = input("First, what is your name? ")

    min = 15
    max = 80
    guess_count = 0
    guesses = list(range(min, max + 1))

    while True:
        if guess_count >= 5:
            print("I give up! I couldn't guess your age.")
            break
        guess = random.choice(guesses)
        response= input((f"Are you {guess} years old? y or n: "))

        if response == 'y':
            print(f"{name} is {guess} years old! Yay!")
            break
        elif response == 'n':
            print("Rats.")
            guesses.remove(guess)
            guess_count += 1
        else: 
            print("Please respond with 'y' or 'n'.")

main()