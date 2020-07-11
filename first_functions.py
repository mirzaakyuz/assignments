def add(a, b):
    print(a + b)

add(3, 5)

def calculator(a, b, c):
    if c == '*':
        print(a * b)
    elif c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        print(a / b)
    else: print('type valid caharacter!')

calculator(5, 2, '/')