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
    bag = "GGGGGBRRRRW"
    purse = 1000
    while purse > 500:
        bet = int(input(f"You have £{purse} left. How much would you like to bet on this round?"))
        if bet > purse:
            bet = int(input(f"You only have £{purse} in your account! Try a lower bet."))
        marble = draw(bag)
        result = ''
        colour = ''
        amount = bet
        if marble == 'G':
            purse += amount
            result = "win"
            colour = "green"
        elif marble == 'B':
            amount = bet * 10
            purse += amount
            result = "win"
            colour = "black"
        elif marble == 'W':
            amount = bet * 5
            purse -= amount
            result = "lose"
            colour = "white"
        else:
            purse -= amount
            result = "lose"
            colour = "red"
        msg = f"You drew a {colour} marble. You {result} £{str(amount)}! Press enter to continue."
        input(msg)
    input("You don't have enough money left to play again. Game over!")

marble_game()