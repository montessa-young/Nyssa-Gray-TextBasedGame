
def armor_price(currency, health):
    while True:
        print("                      ~~~~~~ARMOR~~~~~~")
        print(f"Your wallet has {currency}")
        print(f"Your health level is {health}")
        print("1 Titanium- $700, Makes you shoot and drive slower, add 100 health")
        print("2 leather- $500,Shoot and drive normaly, add 50 health")
        print("3 Paper bag- $250, Shoot and drive boosted by 1.5, add 25 health")
        print("4 No armor- $0, All normal, no added health")

        choice_armor = int(input("What is your choice for armor? Type 1-4: "))

        prices = {
            "titanium":700,
            "leather":500,
            "paper_bag":250,
            "no_armor":0
            }

        if choice_armor == 1:
            currency = currency - prices["titanium"]
            health = health + 100
            print(f"The cost of this armor is 700")
            print(f"Your wallet now has {currency}")
            print(f"Your health is now {health}")
            break

        elif choice_armor == 2:
            currency = currency - prices["leather"]
            health = health + 50
            print(f"The cost of this armor is 500")
            print(f"Your wallet now has {currency}")
            print(f"Your health is now {health}")
            break

        elif choice_armor == 3:
            currency = currency - prices["paper_bag"]
            health = health + 25
            print(f"The cost of this armor is 250")
            print(f"Your wallet now has {currency}")
            print(f"Your health is now {health}")
            break
        elif choice_armor == 4:
            currency = currency - prices["no armor"]
            print(f"The cost of this armor is 0")
            print(f"Your wallet now has {currency}")
            print(f"Your health is now {health}")
            break
        else:
            print("Not a valid input")
    return currency, health


