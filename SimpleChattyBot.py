# A simple bot for a simple conversation.


def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    correct = 0
    while correct <= num:
        print(correct, '!')
        correct = correct + 1


def test():
    print('Let\'s test your programming knowledge.\nWhy do we use methods?')
    print('1. To repeat a statement multiple times.\n2. To decompose a program into several small subroutines.\n3. To '
          'determine the execution time of a program.\n4. To interrupt the execution of a program.')
    user_ans = str(input())
    user_score = 0
    while user_score == 0:
        if user_ans == "2":
            print('Completed, have a nice day!')
            user_score += 1
        else:
            print("Please, try again.")
            user_ans = str(input())


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
end()