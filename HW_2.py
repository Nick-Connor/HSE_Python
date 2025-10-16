# Task 3

word = str(input("Write a word\n"))

print(word[(len(word) - 1) // 2 : (len(word) + 2) // 2])

# Task 4
boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")
