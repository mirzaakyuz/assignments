fib = []

i = 1
x = 0

while x <= 55:
    fib.append(i)
    i += fib[x - 1]
    x += 1
    if fib[x - 1] ==55:
        break
    
print(fib)
