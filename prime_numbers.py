x = int(input('Enter a number: '))
empt_list = []
a = list(range(x+1))
for i in a:
    if i > 1:
        for b in range(2, i // 2 + 1):
            if i % b == 0:
                break
        else:
            empt_list.append(i)
    
    
print(f'prime number in range of {x}: ',empt_list)

