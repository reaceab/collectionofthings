# This is a coffee machine simulator. Buy coffee, fill the machine, take the earnings, check the resources, or decide
# you don't want coffee. Enjoy!

class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"This coffee machine has:\n" \
               f"{self.water} of water\n" \
               f"{self.milk} of milk\n" \
               f"{self.coffee_beans} of coffee beans\n" \
               f"{self.cups} of disposable cups\n" \
               f"${self.money} of money\n" \


    def state(self, action):
        self.action = action
        if self.action == "buy":
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            self.buy(choice)
        elif self.action == "fill":
            add_water = int(input("Write how many ml of water do you want to add: "))
            self.water += add_water
            add_milk = int(input("Write how many ml of milk do you want to add: "))
            self.milk += add_milk
            add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
            self.coffee_beans += add_beans
            add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
            self.cups += add_cups
        elif self.action == "take":
            print("I gave you $" + str(self.money))
            self.money = 0
        elif self.action == "remaining":
            print(self)
        elif self.action == "exit":
            action = "exit"
            return action

    def buy(self, choice):
        self.choice = choice
        if choice == "1":
            if self.water >= 250 and self.milk >= 0 and self.coffee_beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
            elif self.water - 250 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 0 < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough disposable cups!")
        if choice == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
            elif self.water - 350 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough disposable cups!")
        if choice == "3":
            if self.water >= 200 or self.milk >= 100 or self.coffee_beans >= 12 or self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
            elif self.water - 200 < 0:
                print("Sorry, not enough water!")
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
            elif self.coffee_beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
            elif self.cups - 1 < 0:
                print("Sorry, not enough disposable cups!")


machine_state = CoffeeMachine(400, 540, 120, 9, 550)
action = ''
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit): ')
    CoffeeMachine.state(machine_state, action)