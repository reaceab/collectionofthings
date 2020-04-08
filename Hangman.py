# You're hanged!

import random
import string


def menu():
    while True:
        option = input(f'H A N G M A N\nType "play" to play the game, "exit" to quit: ')
        if option == 'play':
            main_game()
        elif option == 'exit':
            break


def main_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    randomizer = random.choice(word_list)
    hint = list("-" * len(randomizer))
    attempts = 0
    attempted_inputs = set()
    while attempts < 8:
        word = ''.join(hint)
        print(f'\n{word}')
        if '-' not in word:
            print('You survived!')
            break
        guess = input('Input a letter: ')
        if guess in randomizer and guess not in word:
            attempted_inputs.add(guess)
            for _ in range(len(randomizer)):
                if randomizer[_] == guess:
                    hint[_] = guess
        elif len(guess) != 1:
            attempted_inputs.add(guess)
            print('You should print a single letter')
        elif guess in attempted_inputs:
            print('You already typed this letter')
        elif guess not in set(string.ascii_lowercase):
            attempted_inputs.add(guess)
            print('It is not an ASCII lowercase letter')
        else:
            attempted_inputs.add(guess)
            print('No such letter in the word')
            attempts += 1
            if attempts == 8:
                print('You are hanged!')


menu()