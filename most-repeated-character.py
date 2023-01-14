# This program finds the most repeated character in a given string
# and displays its frequency
from pprint import pprint
sentence = "This is a common interview question"
char_frequency_dictionary = {}
for char in sentence:
    if char in char_frequency_dictionary:
        char_frequency_dictionary[char] += 1
    else:
        char_frequency_dictionary[char] = 1
char_frequency_sorted = sorted(char_frequency_dictionary.items(),
                               key=lambda kv: kv[1], reverse=True)
print(char_frequency_sorted[0])
