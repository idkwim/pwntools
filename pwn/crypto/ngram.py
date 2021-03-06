from math import sqrt
from pwn import read


english_freq = {}
for i in [2,3]:
    data = read('count_%dl.txt' % (i)).split()
    total = sum(map(int, data[1::2])) * 1.
    english_freq[i] = dict(zip(data[0::2], [int(x) / total for x in data[1::2]]))


def generate_ngram(text, n=3):
    """
    Generate n-gram frequency table for given text.
    """
    occurences = ngram = dict()
    for i in range(len(text)):
        try:
            cur = text[i:i+n]
            if cur in occurences:
                occurences[cur] += 1
            else:
                occurences[cur] = 1
        except IndexError:
            pass

    for (key,value) in occurences.items():
        ngram[key] = float(value) / (len(text) - n + 1)

    return ngram

def dot(a,b):
    """
    Dot product between two dictionaries.
    """
    keys = set(a.keys()).union(set(b.keys()))
    sum = 0
    for i in keys:
        try:
            sum += a[i] * b[i];
        except KeyError:
            pass
    return sum

def norm(a):
    """ Euclidean vector norm """
    sum = 0
    for value in a.values():
      sum += value ** 2
    return sqrt(sum)

def cosine_similarity(a,b):
    """
    Measure of similarity between two vectors in an inner product space. Used for
    comparing n-gram frequency of e.g. english with the n-gram frequency of a given text,
    and thus getting a measure of how close the text is to english.
    """
    return dot(a,b) / (norm(a) * norm(b))


