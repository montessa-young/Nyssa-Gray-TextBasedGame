import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()

print_slow("Welcome to the SUPER DUPER FANTESTICAL MYSTICAL MAGICAL MOON BEAN ICECREAM TAPROOM!")
print(" ")
while True:
    print_slow("We offer a wide variety of drinks and even our very special SLOTS MACHINE!!!")
    print(" ")
    print_slow("Type 1 to order a drink or type 2 to try your luck at the slot game!")
    print(" ")
    choice = int(input("Enter your choice here: "))

    if choice == 1:
        continue

    if choice == 2:
        print_slow("WELCOME TO OUR VERY SPECIAL SLOT MACHINE!!!")
        print(" ")
        print_slow("Heres how it works. We'll have you enter your special number and run two of our die. If your number is equal to them YOU WIN! Otherwise you lose!")
