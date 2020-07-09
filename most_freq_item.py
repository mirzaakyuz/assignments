numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
item = max( numbers, key = numbers.count)
print("The mos frequent number in the list is {} and it's repeated {} times".format(item, numbers.count(item)))
