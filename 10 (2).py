number = int(input("Введите число: "))

print(f"Таблица умножения для {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")