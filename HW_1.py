# Task 1
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} високосный год")
else:
    print(f"{year} не високосный год")

# Task 2

ticket = input()

if len(ticket) != 6:
    print("Ошибка: нужно ввести 6 цифр")
else:
    first_part = ticket[:3]
    second_part = ticket[3:]

sum_first = sum(int(digit) for digit in first_part)
sum_second = sum(int(digit) for digit in second_part)

if sum_first == sum_second:
    print("Счастливый билет!")
else:
    print("Несчастливый билет")
