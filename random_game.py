from sys import argv
from random import randint


class RandGame:
    def __init__(self, num1=1, num2=100):
        self.num1 = int(num1)
        self.num2 = int(num2)
        print(self.game)

    @property
    def game(self):
        rand_num = randint(self.num1, self.num2)
        try:
            guess = int(input(f'Input your guess from {self.num1} to {self.num2}: '))
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


if __name__ == '__main__':
    RandGame(argv[1], argv[2])