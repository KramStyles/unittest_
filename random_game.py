from sys import argv
from random import randint


class RandGame:
    def __init__(self):
        print(self.game)

    @property
    def game(self):
        rand_num = randint(1, 100)
        try:
            guess = int(input('Input your guess: '))
        except ValueError:
            return "Only numbers are allowed"
        else:
            counter = 0
            while guess is not rand_num:
                counter += 1
                if guess > rand_num: print("You are too high")
                elif guess < rand_num: print("You are too Low")
                try:
                    guess = int(input("Don't give up. Try again: "))
                except ValueError:
                    print("Only numbers allowed! Try again")
            return f'You won after {counter} guess(es)'