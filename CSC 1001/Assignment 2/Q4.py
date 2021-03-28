import string


def input_Test():
    while True:
        word = input('Please input a word: ')
        for letter in word:
            if letter not in string.ascii_letters:
                print('Invalid input!')
                break
        else:
            return word


word1 = input_Test()
word2 = input_Test()
wordList1 = list(word1.lower()).sort()
wordList2 = list(word2.lower()).sort()
if wordList1 == wordList2:
    print(word1, 'and', word2, 'is an anagram.')
else:
    print(word1, 'and', word2, 'is not an anagram.')
