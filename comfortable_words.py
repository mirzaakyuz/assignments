left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}

word = str(input("Please write a word: "))

set_word = set(word)

print(set_word)

left_bool = bool(set_word.difference(left))
right_bool = bool(set_word.difference(right))

print((left_bool and right_bool) * f"the word '{word}' is comfortable")
print((not (left_bool and right_bool)) * f"the word '{word}' is not comfortable")