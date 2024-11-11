# # Challenge 1
# # Unsure how to use list comprehension for this
# user_words_inp = input("Input multiple words separated by comma.")
# user_words_inp = user_words_inp.split(',')
# user_words_inp = sorted(user_words_inp)

# print(user_words_inp)

# Challenge 2
user_sentence = input("Input your sentence to return the longest word.")
user_sentence = user_sentence.split()
print(user_sentence)

longest_word = ''

for word in user_sentence:
    if len(word) > len(longest_word):
        longest_word = word
print(f'The longest word is {longest_word}')