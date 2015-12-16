#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

# Sample output using mytext.txt:
#$ python markov.py mytext.txt
#Now, chopping one of all! You're in tummies, you have my factory. I knew just as the wind smells slow-and-sour when the room, and he coughed and the trees, I yelled at all, I called all gummed. So I built,

import random
import sys
import re

#open the file
with open(sys.argv[1],'r') as f:
    contents = f.read()
words = contents.split()

#get length of output
try:
    markovlen = int(sys.argv[2])
except IndexError:
    markovlen = 40


def wordstodict(words):
    d = {}
    for indx in range(len(words)-1):
        try:
            d[words[indx]].append(words[indx+1])
        except KeyError:
            d[words[indx]] = [words[indx+1]]
    return d

def markovgenerator(d,l=markovlen):
    output = []

    #Start with a word that would begin after: '.' or '?' or '!'
    chars = set('!.?')
    current = random.choice(d.keys())
    while not any((c in chars) for c in current):
        current = random.choice(d.keys())
    current = random.choice(d[current])

    #Append words from the dictionary that follow the previous word
    for i in range(l):
        output.append(current)
        current = random.choice(d[current])
    return ' '.join(output)

#create the output
worddict = wordstodict(words)
print markovgenerator(worddict)
