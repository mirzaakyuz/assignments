age = input("please type your age: ")

while not age.isdigit():
    print("You entered in correctly!")
    age = input("Enter your age please: ")
print("Your age is : ", age)
