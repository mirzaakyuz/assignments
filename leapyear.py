year = int(input("Bir yil giriniz: "))
leapyear = (( year % 4 == 0) and ( year % 100 != 0)) or \
     ( year % 400 == 0 )

print( leapyear * f"{year} is a leap year") # when leapyear false it writes 0
print((not leapyear) * f"{year} is not a leap year") 

