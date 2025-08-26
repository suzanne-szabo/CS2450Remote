import random


def main():
    print("I'm going to guess your age!")
    name = input("First, what is your name? ")



    while True:
        guess = random.randint(15, 30)
        response= input((f"Are you {guess} years old? y or n: "))

        if response == 'y':
            print(f"{name} is {guess} years old! Yay!")
            break
        elif response == 'n':
            print("Rats.")
        else: 
            print("Please respond with 'y' or 'n'.")

main()