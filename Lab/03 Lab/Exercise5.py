# Exercise 5: Real-World Application
# 1. Create a program that takes a sentence as input and counts the
# frequency of each word in the sentence.
sentence = "I love I and love and I "
words = sentence.split()
word_count = {}
# 2. Use a dictionary to store the word as the key and the frequency as the
# value.
for word in words: 
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)