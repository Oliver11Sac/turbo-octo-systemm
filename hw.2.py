div_by_5 = [i for i in range(1, 51) if i % 5 == 0]
print(div_by_5)


text = "Привет, мир!"
vowels = [ch for ch in text.lower() if ch in "аеёиоуыэюя"]
print(vowels)


codes = [ord(ch) for ch in "Python"]
print(codes)


fruits = ["яблоко", "банан", "киви", "апельсин"]
long_fruits = [f for f in fruits if len(f) > 5]
print(long_fruits)


cubes = [i**3 for i in range(1, 11)]
print(cubes)


nums = [0, 1, 2, 3, 4, 5]
strings = [f"Число: {n}" for n in nums]
print(strings)


numbers = [1, -2, 3, -4, 5]
positives = [n for n in numbers if n > 0]
print(positives)