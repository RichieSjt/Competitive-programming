import itertools

def offsets(word):
    offset_words = []


    for i in range(1, len(word)):
        offset_word = ""
        offset = i
        
        offset_word += word[offset]
        offset = (offset + 1) % len(word)

        while offset != i:
            offset_word += word[offset]
            offset = (offset + 1) % len(word)

        offset_words.append(offset_word)

    return offset_words


n = int(input())
counter = 0

words = [word for word in input().split()]
words_sorted = []

for word in words:
    sorted_word = ""
    x = sorted([char for char in word])
    for char in x:
        sorted_word += char
    words_sorted.append(sorted_word)

len_w = len(words)
i = 0
j = i + 1

while i < len_w:
    offset = offsets(words[i])
    while j < len_w:
        
        print(words[i])
        print(words[j])

        if words_sorted[i] == words_sorted[j]:
            if words[j] in offset:
                len_w -= 1
                del words[j]
                del words_sorted[j]
        j += 1
    j = i + 1
    i += 1

print(len(words))