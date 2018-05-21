import json
import nltk
import operator
import re
import sys

word_list = []

with open("review.json") as myfile:
    head = [next(myfile) for x in range(10000)]

word_list = re.sub("[^\w]", " ",  ' '.join(head)).split()
cleaned_words = [w.lower() for w in word_list if w.isalnum()]


def getsentence(root, n, forward_direction):

    if n <= 0:
        return root

    bgs = nltk.bigrams(cleaned_words)

    sun_bigrams = [b for b in bgs if (b[1-forward_direction] == root)]

    fdist = nltk.FreqDist(sun_bigrams)

    sorted_x = sorted(fdist.items(), key=operator.itemgetter(1))
    word = sorted_x[len(sorted_x)-1][0][forward_direction]

    if forward_direction == 1:
        return root + ' ' + getsentence(word, n-1, forward_direction)
    else:
        return getsentence(word, n-1, forward_direction) + ' ' + root


# initial defaults
start = "chocolate"
n = 5
forward_direction = 1

# apply arguments
if(len(sys.argv) > 1):
    start = sys.argv[1]
if(len(sys.argv) > 2):
    n = int(sys.argv[2])
if(len(sys.argv) > 3):
    forward_direction = int(sys.argv[3])


print(getsentence(start, n, forward_direction))
