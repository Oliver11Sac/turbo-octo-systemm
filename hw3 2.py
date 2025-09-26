products = {1:"Футболка",2:"Кроссовки",3:"Шапка"}
cart = []

while True:
    c = input("\n1-Товары 2-Добавить 3-Удалить 4-Заменить 5-Корзина 0-Выход: ")
    if c=="1": print(products)
    elif c=="2": cart.append(products.get(int(input("ID: ")), "Нет товара"))
    elif c=="3" and cart: cart.pop(int(input("Номер в корзине: "))-1)
    elif c=="4" and cart: cart[int(input("Номер: "))-1] = products.get(int(input("Новый ID: ")), "Нет товара")
    elif c=="5": print(cart)
    elif c=="0": break