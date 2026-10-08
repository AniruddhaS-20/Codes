def largest(*number):
    maximum = number[0]

    for numbers in number:
        if numbers > maximum:
            maximum = numbers

    print("Largest number:", maximum)


largest(85, 72, 89, 45)