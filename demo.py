# christopher = {}
# christopher['first'] = 'Christopher'
# christopher['last'] = 'Harrison'

# susan = {}
# susan['first'] = 'Susan'
# susan['last'] = 'Ibach'

# people = []
# people.append(christopher)
# people.append(susan)
# people.append({ 'first' : 'Bill', 'last' : 'Gates'})

# print(people)

# family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
# family_members = tuple(family_members)
# print(family_members)

# if True:
#     print('it is true')

# empty_seat = 14

# if empty_seat > 3:  # in this case, 14>3=True, so the body will execute
#     print('there is still seat to sit')

# x = 6
# y = 9
# print ("is x equal to y?                 :" , x == y)
# print ("is x not equal to y?             :" , x != y)
# print ("is x less than y?                :" , x < y)
# print ("is x greater than y?             :" , x > y)
# print ("is x less than or equal to y?    :" , x <= y)
# print ("is x greater than or equal to y? :" , x >= y)

# number = 2
# if number <= 3:    
#     print("Number is smaller than or equal to 3") 
# else:  # Optional clause (you can only have one else)
#     print("Number is bigger than 3")


# number = 9

# if number >= 10:
#     print('The number is equal or greater than 10')
# else:
#     print('The number is less than 10.')


# audience_group = 'kid', 'teen', 'adult' # this is tuple
# print(type(audience_group))

# audience = "teen"

# if audience in audience_group:
#     if audience == "kid":
#         print("it is free to go to cinema")
#     elif audience == "teen":
#         print("discounted price!")
#     else: # audience == "adult":
#         print("normal price")
# else:
#     print("No such audience, stay at your home!")



# #####################
# score = int(input("Enter your score : "))

# if score >= 90:
#     if score >= 95:
#         Score_letter="A+"
#     else:
#         Score_letter="A"
# elif score >= 80:
#     if score >= 85:
#         Score_letter="B+"
#     else:
#         Score_letter="B"
# else:
#     Score_letter="below B"

# print ("Your degree: %s" % Score_letter)
####################




##############

# province = str(input("Which state you live?:  "))


# if province.lower() == 'alberta' or 'nanavut':
#     tax = 0.05
# elif province.lower() == 'ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print('tax = ', tax)

##########

# answer = 44

# question = 'What number am I thinking of?  '
# print ("Let's play the guessing game!")

# while True:
#     guess = int(input(question))

#     if guess < answer:
#         print('Little higher')
#     elif guess > answer:
#         print('Little lower')
#     else:  # guess == answer
#         print('Are you a MINDREADER!!!')
#         break
#################

# flowers = ['Rose', 'Orchid', 'Tulip']
# count1 = len(flowers)
# count2 = 0

# while count2 < count1:
#     print(flowers[count2])
#     count2 += 1 # !!!!
##############
### for loop
###
# for variable in iterable :
#     code block
##################
# for i in [1, 2, 3, 4, 5] :
#     print(i)

# for i in {'n1' : 'one', 'n2' : 'two'} : print(i)

# seasons = ['spring', 'summer', 'autumn', 'winter']

# for season in seasons :
#     print(season)

# iterable = [1, 2, 3, 4]

# for i in iterable:
#     print(i**2)
    
# ###############
# course = '123456'

# for i in course :
#     print(i)

######

# n = int(input('enter a number between 1-10'))

# for i in range(11):
#     print('% d x % d = ' % (n, i), n*i )

###################

# x = 55
# sayi = 0
# while sayi < x:
#     sayi = int(input("Please enter higher number: "))
# while sayi > x:
#     sayi = int(input("Please enter lover number: "))
# print(f"you found the number {x}")

#############

# sentence = str(input("insert a sentence: "))

# list_sentence = sentence.split()



# print("The longest word in your sentence is: ", max(list_sentence, key=len),\
#      "with a length of ", len(max(list_sentence, key=len)))



# number = int(input('Please enter a number: '))
# i = 0
# a = list([*range(number)])
# #print(a)

# while i < len(a):
#     print(i**2)
#     i += 1

# sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

# for item in sample_list:
#     print(f"The type of {item} is {type(item)}")

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]


ratings_1 = row_1[4]
ratings_2 = row_2[4]
ratings_3 = row_3[4]

total = ratings_1 + ratings_2 + ratings_3

average = total / 3

print(average)