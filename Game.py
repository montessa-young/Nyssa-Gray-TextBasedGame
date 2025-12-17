from intro import start_game
from Bar import bar_scene
from armor import armor_price
currency = 1000
health = 10

start_game()
while health >= 10:
    bar_scene(currency, health)
    armor_price(currency,health)
    bar_scene(currency, health)

print("Game Over")



