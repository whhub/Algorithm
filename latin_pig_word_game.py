# coding=utf8
"""
给定一个单词，从左往右统计，将单词字母中第一个元音字母之前的单词，移动到词尾，移动完毕之后再在新组成的单词词尾添加“ay”
"""


def latin_pig_word_game(word):
    first_vowel_index = find_first_vowel(word)
    head = word[:first_vowel_index]
    tail = word[first_vowel_index:]
    return tail + head + "ay"


def find_first_vowel(word):
    vowels = "aeiou"
    len_word = int(len(word))
    for i in range(len_word):
        if word[i] in vowels:
            return i
    return 0


print("Latin pig word games: ")
aword = "object"
print("'%s' changes to : '%s'" % (aword, latin_pig_word_game(aword)))
aword = "hello"
print("'%s' changes to : '%s'" % (aword, latin_pig_word_game(aword)))
aword = "xyz"
print("'%s' changes to : '%s'" % (aword, latin_pig_word_game(aword)))
aword = ""
print("'%s' changes to : '%s'" % (aword, latin_pig_word_game(aword)))
