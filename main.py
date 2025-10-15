'''Мини-игра: угадай число'''
import random

numbers = [3, 4, 2, 1, 8, 32, 12, 54, 76, 10]
secret = random.choice(numbers) # Секрет
attempts = 3 # Попытки

print(f"Попробуй угадать число из списка {numbers}")
while attempts > 0:
    guess = int(input("Ваше число: ")) # Ввод искомого числа
    if guess == secret:
        print("Вы победили 🎉")
        break
    else:
        attempts -= 1
        if guess < secret:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

        if attempts == 0:
            print("Вы проиграли,ваши попытки закончились 😢")
        else:
            print(f"Количество попыток {attempts}")







