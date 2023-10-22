# Зчитуємо введене користувачем число у форматі XXXXX
number = input("Введіть ціле число у форматі XXXXX: ")

digits = []

for digit in number:
    digits.append(int(digit))

max_digit = max(digits)

for i in range(max_digit, 0, -1):
    for digit in digits:
        if digit >= i:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()  # Перехід на новий рядок після виведення кожного рядка гістограми

# Виводимо числові значення розрядів
print(*digits)
