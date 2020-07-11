while True:
    age = input("Are you a cigarette addict older than 75 years old? (Yes/No): ")
    chronic = input("Do you have a severe chronic disease? (Yes/No): ")
    immune = input("Is your immune system too weak? ()Yes/No: ")

    a = list(age)[0].capitalize() 
    c = list(chronic)[0].capitalize() 
    i = list(immune)[0].capitalize()
    if (a not in ['N', 'Y']) or (c not in ['N', 'Y']) or (i not in ['N', 'Y']):
        print("Please type valid answer!")
    else:
        break  

if a == 'Y' or c == 'Y' or i == 'Y':
    print('You are in risky group')
else:
    print('You are not in risky group')

