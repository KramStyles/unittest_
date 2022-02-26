from sys import argv
from random import randint


class RandGame:
    def __init__(self, num1=1, num2=100):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.rand_num = randint(self.num1, self.num2)
        self.counter = 0
        print(self.game)
    
    def guess(self, random_guess):
        if random_guess > self.rand_num:
            print("You are too high")
        elif random_guess < self.rand_num:
            print("You are too Low")
        try:
            guess = int(input("Don't give up. Try again: "))
        except ValueError:
            print("Only numbers allowed! Try again")

        return f'You won after {self.counter} guess(es)'

    @property
    def game(self):
        try:
            guess = int(input(f'Input your guess from {self.num1} to {self.num2}: '))
        except ValueError:
            return "Only numbers are allowed"
        else:
            while guess is not self.rand_num:
                self.counter += 1
                return self.guess(guess)


if __name__ == '__main__':
    RandGame(argv[1], argv[2])