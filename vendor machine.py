class CoffeeMachine:

    running = False

    def __init__(self,customer, water, milk, coffee_beans, cups):
        # quantities of items the coffee machine already had
        self.customer=customer
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups


        # if the machine isnt running then start running
        if not CoffeeMachine.running:
            self.start()


    def start(self):
        self.running = True  # it is running as to not trigger the start() in initialiser method
        self.action = input("Write action (buy, fill, remaining, exit):\n")
        print()

        # possible choices to perform in the coffee machine
        action_choices = {"buy": self.buy, "fill": self.fill, "exit": exit, "remaining": self.status}

        if self.action in action_choices:
            action_choices[self.action]()
        else:
            exit()


    def return_to_menu(self):  # returns to the menu after an action
        print()
        self.start()

    def available_check(self):  # checks if it can afford making that type of coffee at the moment

        self.not_available = ""  # by checking whether the supplies goes below 0 after it is deducted
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee_beans - self.reduced[2] < 0:
            self.not_available = "coffee beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "disposable cups"

        if self.not_available != "":  # if something was detected to be below zero after deduction
            print(f"Sorry, not enough {self.not_available}!")
            return False
        else:  # if everything is enough to make the coffee
            print("I have enough resources, making you a coffee!")
            return True

    def deduct_supplies(self):  # performs operation from the reduced list, based on the coffee chosen
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee_beans -= self.reduced[2]
        self.cups -= self.reduced[3]

    def buy(self):
        self.customer += str(input("enter the customer name:\n"))
        self.choice = input("What do you want to buy?\n 1 - espresso\n 2 - latte\n 3 - cappuccino\n back - to main menu:\n")
        if self.choice == '1':
            self.reduced = [250, 0, 16, 1]  # water, milk, coffee beans, cups
            if self.available_check():  # checks if supplies are available
                self.deduct_supplies()  # if it is, then it deducts

        elif self.choice == '2':
            self.reduced = [350, 75, 20, 1]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "3":
            self.reduced = [200, 100, 12, 1]
            if self.available_check():
                self.deduct_supplies()

        elif self.choice == "back":
            self.return_to_menu()

        self.return_to_menu()

    def fill(self):  # for adding supplies to the machine
        self.customer += str(input("enter the customer name:\n"))
        self.water += int(input("Write how much water do you want to add:\n"))
        self.milk += int(input("Write how much milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.return_to_menu()


    def status(self):  # to display the quantities of supplies in the machine at the moment
        print(f"The coffee machine has:")
        print(f"{self.water}ml of water")
        print(f"{self.milk}ml of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} no of disposable cups")
        self.return_to_menu()


CoffeeMachine("john",400, 540, 120, 9)  # specify the quantities of supplies at the beginning
