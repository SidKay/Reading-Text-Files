# A simple program that counts the number of words in a given text 
# and returns the number of each word used.

# Made by Obinna Anya
# Student ID: I4G006421ROU

def read_file_content(filename):
    # This function reads the file provided as an argument
    with open(filename) as f:
        lines = f.read()
        return lines

def count_words():
    # Here, the words in the file is split into a list
    text = read_file_content('story.txt')
    words = text.split()
    pureWords = []

    # I noticed that some words still had punctuation marks attached to them
    # So here, the punctuation marks get removed
    # Words with capital letters are also changed to lower case letters
    # Then the word gets added to the 'pureWords' list
    for word in words:
        a = word.strip(',.?').lower()
        pureWords.append(a)

    # This counts the number of occurences of a word in the 'pureWords' list and retuns them in a dictionary
    wordCounter = dict((i, pureWords.count(i)) for i in set(pureWords))
    print(wordCounter)
    return

count_words()