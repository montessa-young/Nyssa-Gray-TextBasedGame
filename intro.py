import time



def start_game() :
    def print_slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.06)
        print()
    print_slow("Explore space, discover new planets, defeat aliens, and dodge through the asteroid belts, but")
    print_slow("be careful about trusting new people; you never know what can happen. You will have some")
    print_slow("choices of weapons and armor. Just know that the weapons and your armor will affect how you")
    time.sleep(1)
