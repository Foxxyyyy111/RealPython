word = input("Enter a word: ")

vowel_count = 0
for character in list(word):
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
       vowel_count += 1

print("This word", word, "contains", vowel_count, "vowels")