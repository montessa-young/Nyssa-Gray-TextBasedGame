import random
import time
#Still needs a wallet added from a seperate file. Ask miss.
#lines 33
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
        continue

    if choice == 2:
        print_slow("WELCOME TO OUR VERY SPECIAL SLOT MACHINE!!!")
        print(" ")
        print_slow("Heres how it works. We'll have you enter the amount you want to bet and your special number and run two of our die. If your number is equal to them YOU WIN! Otherwise you lose!")
        print(" ")
        bid_amount = int(input("Enter the amount you want to bid: "))
        #new_balance = balance - bid_amount
        #print_slow(new_balance)
        lucky_number = int(input("Enter your lucky number here: "))
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(" ")
        print_slow("The first slot reads...")
        print_very_slow(f"......{die_1}!")
        print_slow(f"The second slot reads...")
        print_very_slow(f"......{die_2}!")
    if choice == 3:
        print_slow("Are you sure????")
        leave = int(input("Type 1 for yes and 2 for no: "))
        if leave == 1:
            print_slow("Alright then:(")
            break
        if leave == 2:
            print_slow("BET!!!")



