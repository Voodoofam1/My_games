'''Мини-игра: угадай число'''
numbers = [3, 4, 2, 1, 8, 32, 12, 54, 76, 10]
secret = numbers[7] # Секрет
attempts = 3 # Попытки

print(f"Попробуй угадать число из списка {numbers}")
while attempts > 0:
    guess = int(input("Ваше число: ")) # Ввод искомого числа
    if guess == secret:
        print("Вы победили 🎉")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Вы проиграли,ваши попытки закончились 😢")
        else:
            print(f"Количество попыток {attempts}")





