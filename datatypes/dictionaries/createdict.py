#Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
#dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
#check whether a string is in the dictionary.

f = open('words.txt')

def createdict(inputf):
    d = {}
    for key in f:
        if key not in d:
            d[key.strip()] = '' 
    return d

print(createdict(f))
