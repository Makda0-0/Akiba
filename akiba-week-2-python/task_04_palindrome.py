word = input("Enter a word: ")
lower_word = word.lower()

if lower_word == lower_word[::-1]:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")