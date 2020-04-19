def number_list(number):
    i = 0
    numbers = []

    while i < number:
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)


    print("The numbers: ")

    for num in numbers:
        print(num)


number_list(10)
