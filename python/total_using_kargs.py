def total(**numbers):
    sum = 0

    for value in numbers.values():
        sum += value

    print("Total =", sum)


total(a=10, b=20, c=30, d=40)