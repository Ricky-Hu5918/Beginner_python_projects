import random
import time

def play():
    elements = ['r', 'p', 's']
    user = input("What's your choice? (r for rock, p for paper, s for scissors): ").lower()
    while user not in elements:
        print("\nPlease check your input!! (r for rock, p for paper, s for scissors)")
        user = input("What's your choice? (r for rock, p for paper, s for scissors): ").lower()

    computer = random.choice(elements)
    print("......")
    time.sleep(0.5)

    if user == computer:
        return print(f"It\'s a tie!! Your choice was {user}, and the computer's choice was {computer}")

    if is_win(user, computer) == True:
        return print(f"You won!! Your choice was {user}, and the computer's choice was {computer}.")
    else:
        return print(f"You lost!! Your choice was {user}, the computer's choice was {computer}.")

#rules: r > s, s > p, p > r
def is_win(player, component):
    #return true if player wins
    if (player == 'r' and component == 's') or (player == 's' and component == 'p') \
        or (player == 'p' and component == 'r'):
        return True
    else:
        return False

#print(play())

def main():
    start = input("You want to play this game? Type \"y\" to start or anything else to quit!! ").lower()

    while start == 'y':
        print("\nGame is loading ......\n")
        time.sleep(1)
        print("Great! Input your choice and let see if you can beat the computer!!!")

        play()
        start = input("\nWant to play again? Type \"y\" to start or anything else to quit!! ").lower()


#run game
main()

