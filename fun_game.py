import random

start = ("Телега","Водитель","Каждый птушник")
middle = ("ест","катится","крутит руль")
finish = ("сигарета","водофон","сержант Галя")
for word in range(4):
    a = random.choice(start)
    b = random.choice(middle)
    c = random.choice(finish)
    print(a, b, c)