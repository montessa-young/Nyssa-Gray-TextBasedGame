<<<<<<< HEAD
from intro import print_slow, start_game
from Bar import bar, print_very_slow
from armor import armor_price

def bar_scene():
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.06)
        print()
    def print_very_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(1.00)
        print()


    print_slow("Welcome to the SUPER DUPER FANTESTICAL MYSTICAL MAGICAL MOON BEAN ICECREAM TAPROOM!")
    print(" ")
    while True:
        print_slow("We offer a wide variety of drinks and even our very special SLOTS MACHINE!!!")
        print(" ")
        print_slow("Type 1 to order a drink or type 2 to try your luck at the slot game! If you're tryna leave....YOU SUCK and we hate you:( but type 3 I guess:(((")
        print(" ")
        choice = int(input("Enter your choice here: "))

        if choice == 1:
            print_slow("An old man comes from behind the bar...'WELCOME AND HOWDY BUDDY WHAT CAN I GET FOR YOU????")
            print_slow("FOR SALE WE HAVE...")
            print("1) MODELO~~~$10")
            print("2) BUDLIGHT~~~$15")
            print("3) WISKEY~~~$25")
            print("4) APPLE JUICE~~~$6")
            print("5) MARGARITA~~~$67")
            print("6) MONSTER!!!!!!!~~~$2")
            print("7) CORONA~~~$15")
            print("8) AQUA~~~$1")
            drinky = int(input("Enter the number of the drink you want to try: "))
            if drinky == 1:
                print_slow("'ONE MODELO COMING UP, THAT'LL BE $10'")
                wallet - 10
            if drinky == 2:
                wallet - 15
                print_slow("'ONE BUDLIGHT COMING UP, THAT'LL BE $15'")
            if drinky == 3:
                wallet - 25
                print_slow("'ONE WISKEY COMING UP, THAT'LL BE $25'")
            if drinky == 4:
                wallet - 6
                print_slow("'ONE APPLE JUICE COMING UP, THAT'LL BE $6'")
            if drinky == 5:
                wallet - 67
                print_slow("'ONE MARGARITA COMING UP, THAT'LL BE $67'")
            if drinky == 6:
                wallet - 2
                print_slow("'ONE MONSTER!!!!!! COMING UP, THAT'LL BE $2'")
                print_slow("'FOR SALE WE HAVE THESE THREE OPTIONS: ")
                print_slow("1) White Monster")
                print_slow("2)VIKING BERRY MONSTER:)")
                print_slow("3) Pipeline Punch Monster")
                monster = int(input("Enter your choice of monster here: "))
                print_slow("I HEARD ONE VIKING BERRY MONSTER")
            if drinky == 7:
                wallet - 15
                print_slow("'ONE CORONA COMING UP, THAT'LL BE $15'")
            if drinky == 8:
                wallet - 1
                print_slow("'ONE CUP OF AQUA COMING UP, THAT'LL BE $1'")
        if choice == 2:
            print_slow("WELCOME TO OUR VERY SPECIAL SLOT MACHINE!!!")
            print(" ")
            print_slow("Heres how it works. We'll have you enter the amount you want to bet and your special number and run two of our die. If your number is equal to them YOU WIN! Otherwise you lose!")
            print(" ")
            bid_amount = int(input("Enter the amount you want to bid: "))
            lucky_number = int(input("Enter your lucky number here (1-6): "))
            die_1 = random.randint(1,6)
            die_2 = random.randint(1,6)
            print(" ")
            print_slow("The first slot reads...")
            print_very_slow(f"......{die_1}!")
            print_slow(f"The second slot reads...")
            print_very_slow(f"......{die_2}!")
            if lucky_number == die_1 or lucky_number == die_2:
                print("YOU WIN!!! The multiplier added is 2x")
                new_amount = bid_amount * 2
                new_wallet = new_amount + wallet
                print(f"Your new wallet total is {new_wallet}")
            if lucky_number == die_1 and lucky_number == die_2:
                print("OH WOW THEY BOTH MATCH!!! YOUR MULTIPLIER IS 5X")
                new_amount = bid_amount * 5
                new_wallet = new_amount + wallet
                print(f"Your new wallet total is {new_wallet}")
            if lucky_number != die_1 and lucky_number != die_2:
                print("You lost:( Your money has been subtracted")
                new_wallet = wallet - bid_amount
                print(f"Your new wallet total is {new_wallet}")
        if choice == 3:
            print_slow("Are you sure????")
            leave = int(input("Type 1 for yes and 2 for no: "))
            if leave == 1:
                print_slow("Alright then:(")
                break
            if leave == 2:
                print_slow("BET!!!!")


=======
from intro import start_game
from Bar import bar_scene
from armor import armor_price
currency = 1000
health = 100
>>>>>>> 70b0c3c996fb7a2ddd8d698c7308bbd804412923
start_game()
armor_price(currency, health)
bar_scene()