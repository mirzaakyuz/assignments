# while True:
#     try:
#         # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
#         age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         #better try again... Return to the start of the loop
#         continue
#     else:
#         #age was successfully parsed!
#         #we're ready to exit the loop.
#         break
# if age >= 18: 
#     print("You are able to vote in the United States!")
# else:
#     print("You are not able to vote in the United States.")


# def texter(text1, text2, text3):
#     print(f"{text2} {text3} {text1}")

# texter( text2 = 'a', text3 = 'b', text1 = 'c')

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot( 100 , 'as')

# def slicer(*num):
#     odd=[]
#     even=[]
#     for i in num:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print(even)
#     print(odd)

# def slicer(*num):
#     odd=[i for i in num if i%2 !=0]
#     even=[i for i in num if i%2 ==0]
#     print(even)
#     print(odd)


# def slicer(*num):
#     a=[]
#     b=[]
#     for i in num:
#         if i%2 == 0:
#             a.append(i)
#         else:
#             b.append(i)
#     print('cift', a)
#     print('tek',b)
    
    
# listem = {a ='one',b = 'two',c = 'three'}

# print(listem)
# def organ(**var):
#     names = []
#     age = []
#     for key, val in var.items():
#         names.append(key)
#         age.append(val)
#     print(names)
#     print(age)

# organ( Beth=25, James=23)

# def brothers(bro1,bro2,bro3):
#     print('here are the names of brothers : ')
#     print(bro1,bro2,bro3, sep = '\n')

# family = ['tom', 'sue', 'helm']
# brothers(*family)

# def merger(values0, values3, values2, values1):
#     print('For me,', values0, values3, values2, values1, 'are genius.')

# genius = ('bill', 'rossum', 'guido van', 'gates')

# merger(*genius)

# def gene(x, y):
#     print(x, "belongs x")
#     print(y, "belongs y")

# dict_gene = {'y':'mary', 'x' : 'james'}

# gene(**dict_gene)


# def meaner(Serra,Harun,Nil):
#     avg_ages=(Serra+Harun+Nil)/len(friends.values())
#     print("The average of my friends is : ", avg_ages)
# friends={"Serra": 32,"Harun" : 30, "Nil": 25}
# meaner(**friends)

# str1 = 'hello'
# print(str1[-1:])

# print(r"\nhello")

# print("new" "line", 2)

from random import choice

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(choice(city))  

import math
print(dir(math))

import random
print(random.random())