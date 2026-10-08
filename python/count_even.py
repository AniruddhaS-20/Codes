def count_even(*numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    print("Even numbers count:", count)


count_even(10, 15, 20, 25, 30, 35, 40)