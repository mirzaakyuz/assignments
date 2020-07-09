a = input("I am Armstrong Number Kontroller, please type an integer: ")

if not a.isnumeric():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    sum = 0
    i = len(a)
    # print(i)
    list_num = list(a)
    list_num_int = []
    # print(list_num)
    for b in range(i):
            list_num_int.append(int(list_num[b]))
            sum += list_num_int[b] ** i
    if sum == int(a):
            print(f"{a} is an Armstrong number.")
    else:
        print(f"{a} is not an Armstrong number.")
