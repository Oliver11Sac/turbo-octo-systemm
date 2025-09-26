
nums = [i for i in range(1, 11)]
print(nums)

squares = [i**2 for i in range(1, 11)]
print(squares)


evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)


letters = [ch for ch in "Happy"]
print(letters)


words = ["имя", "фамилия", "отчество"]
lengths = [len(w) for w in words]
print(lengths)


odd_squares = [i**2 for i in range(1, 11) if i % 2 != 0]
print(odd_squares)


words = ["привет", "как дела", "что делаешь"]
upper_words = [w.upper() for w in words]
print(upper_words)