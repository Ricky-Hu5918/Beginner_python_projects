import random

def guess_number_usr(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))

        if guess_number > random_number:
            print("Sorry, guess again! Too high!!\n")
        elif guess_number < random_number:
            print("Sorry, guess again! Too low!!\n")

    print(f"Yeah! You have guessed the number {random_number} correctly!!!")

#guess_number_usr(10)


def guess_number_computer(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low   #could also be high

        feedback = input(f"The number computer guessed is {guess_number}. Is it too high (H), too low (L), or correct (C)??: ").lower()
        if feedback == "h":
            high = guess_number - 1
        elif feedback == "l":
            low = guess_number + 1

    print(f"Yeah! The computer have guessed the number {guess_number} correctly!!!")

guess_number_computer(1000)