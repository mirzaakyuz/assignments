a = int(input("I am Prime-Checker, please type a number: "))
if a > 1:
    for b in range(2, a // 2 + 1):
        if a % b == 0:
            print( f"{a} is not prime" )
            break
    else:
        print( f"{a} is prime")
else:
    print(f"{a} is not prime")
    

