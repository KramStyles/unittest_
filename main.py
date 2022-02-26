import utility
import shop
from random_game import RandGame
from pyjokes import get_jokes

# print(utility.add(56, 23))
# print(utility.minus(56, 23))
# print(shop.buy('Money, Video Games, onions, tuRN'))


if __name__ == '__main__':
    # RandGame()
    for jokes in get_jokes('en', 'all'):
        print(jokes)
