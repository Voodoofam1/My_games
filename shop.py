

products = ["молоко", "сыр", "мороженое", "хлеб", "мясо","яйца"]
prices = [3.26, 5.63, 3.25, 4.90, 13.23,5]
total = 0

print("Добро пожаловать в магазин Евроопт")
print("Наши товары: ")
for i in range(len(products)):
    print(i +1,"-",products[i],"-",prices[i],"рублей")

while True:
    choice = input("Выберите товар по номеру (или нажмите 'стоп')")
    if choice == "стоп":
        break
    index = int(choice)-1
    total += prices[index]
    print("В корзину положил: ",products[index], "Сумма: ", total)
print("Итого к оплате: ", total, "рублей")
