import random
def game():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    start = input("What do you choose? Rock, Paper or scissor?" " ")
    RPS = [rock, paper, scissors]
    AIresponse = random.randint(0, 2)
    AIRPS = RPS[AIresponse]
    if start == "scissor":
        print(f"You selected\n {scissors}\n" + f"The computer has selected\n {AIRPS}")
        if AIresponse == 0:
            print("You lose")
        elif AIresponse == 1:
            print("You Win")
        else:
            print("You draw")
    elif start == "paper":
        print(f"You selected\n {paper}\n" + f"The computer has selected\n {AIRPS}")
        if AIresponse == 0:
            print("You Win")
        elif AIresponse == 1:
            print("You draw")
        else:
            print("You Lose")
    elif start == "rock":
        print(f"you selected\n {rock}\n" + f"The computer has selected\n {AIRPS}")
        if AIresponse == 0:
            print("You draw")
        elif AIresponse == 1:
            print("You lose")
        else:
            print("You win")
    else:
        print("This is invalid")

    go_again = input("Type DONE to close, and AGAIN to try again: ")
    go_again_Low = go_again.lower()
    if go_again_Low == "again":
        game()
    elif go_again_Low == "done":
        print("Goodbye")
    while go_again != "again" and go_again != "done":
        print("That is an invalid answer, let us try again:")
        go_again = input("Type DONE to close, and AGAIN to try again: ")
        go_again_Low = go_again.lower()
        if go_again_Low == "again":
            game()
        elif go_again_Low == "done":
            print("Goodbye")

game()



