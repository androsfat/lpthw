def number_list(number, step=1):
    i = 0
    numbers = []

    while range(i, number):
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)


    print("The numbers: ")

    for num in numbers:
        print(num)


number_list(12, 3)
