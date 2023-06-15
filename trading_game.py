# Create a marble betting game
    # a bag has 10 marbles: 6 green and 4 red
    # if you draw a green marble, you win the same amount that you bet
    # if you draw a red marble, you lose the amount that you bet
    # marbles are replaced after each round
    # before each draw decide how much you want to bet and enter it
    # you start the game with £1000
    # if you lose half of your money the game is over
    # print/show data as you go
        # NB. use input prompt in Scrimba

    # Bonus: replace 2 marbles, 1 green with 1 black (10x winner) marble and 1 red with 1 white (5x loser marble)

from random import choice as draw

def marble_game():
    bag = "GGGGGGRRRR"
    purse = 1000
    while purse > 500:
        bet = int(input("How much would you like to bet on this round?"))
        marble = draw(bag)
        result = ''
        if marble == 'G':
            purse += bet
            result = "win"
        elif marble == 'R':
            purse -= bet
            result = "lose"
        msg = f"You drew a %s marble. You {result} £{str(bet)}! Press enter to continue." %("green" if marble == "G" else "red")
        input(msg)
    input("You don't have enough money left to play. Game over!")

marble_game()