cars = {
    "bmw": "надёжный немецкий автомобиль 💖",
    "ferrari": "итальянский жеребец 🐎  ",
    "audi": "властелин колец ⭕⭕⭕⭕",
    "ford": "амерканский суперкар 💲"
}

print(f"Приветствую вас в салоне автомобилей 🚕")
print(f"Команды: показать, добавить, узнать, выйти")

while True:
    command = input("введите команду из списка ⬆").lower()

    if command == "показать":
        print("\n список машин: ")
        for car in cars:
            print(car,"=*=", cars[car])

    elif command == "добавить":
        new_car = input("введите марку машины: ").lower()
        info = input("опишите машину: ").lower()
        cars[new_car] = info
        print("автомобиль добавлен в салон ✅")

    elif command == "узнать":
        name = input("Введите марку машины: ").lower()
        if name in cars:
            print(name,"=*=", cars[name])
        else:
            print("такого авто нет ❌")

    elif command == "выйти":
        print("до встречи! ")
        break

    else:
        print("ошибка ❗\nтакой команды нет")














