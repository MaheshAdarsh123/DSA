def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    count1 = {}
    count2 = {}

    for char in word1:
        count1[char] = count1.get(char,0)+1

    for char in word2:
        count2[char] = count2.get(char,0)+1

    return count1 == count2

word1 = input('word1 --> ')
word2 = input('word2 --> ')
print(is_anagram(word1, word2))
