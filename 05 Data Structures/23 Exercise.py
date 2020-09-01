# 23 Exercise

# Write a program to find the most repeated character in this sentence
from pprint import pprint

sentence = "This is a commom interview question"

char_frequency= {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# print(char_frequency)
# pprint(char_frequency, width = 1)

tuple_sentence = char_frequency.items()
tuple_sentence_sorted = sorted(tuple_sentence, key=lambda kv:kv[1], reverse=True)

print(tuple_sentence_sorted)
print(tuple_sentence_sorted[0])