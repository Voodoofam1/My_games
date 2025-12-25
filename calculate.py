def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "ошибка! делить на 0 нельзя"
    return a / b

def calculate():
    print("калькулятор 📅")
    print("выберите действие")
    print("1 - сложение")
    print("2 - вычитание")
    print("3 - умножение")
    print("4 - деление")

    choice = input("введите номер операции от 1 до 4: ")
    if choice not in ("1", "2", "3", "4"):
        print("такой операции не сущестуевт")
        return
    a = float(input("введите первое число: "))
    b = float(input("введите второе число: "))
    if choice == "1":
        print("результат: ", add(a, b))

    elif choice == "2":
         print("результат: ", sub(a, b))
    elif choice == "3":
        print("результат: ", mul(a, b))
    elif choice == "4":
        print("результат: ", div(a, b))
    else:
        print("такой операции не существует")


for vizov in range(1, 4):
    calculate()


