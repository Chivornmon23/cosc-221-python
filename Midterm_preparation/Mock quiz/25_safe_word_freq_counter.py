def word_frequncies(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequncies("I love you, but you dont you because you and you"))