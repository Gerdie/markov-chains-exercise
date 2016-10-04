from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as open_file: 
        return open_file.read()

def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for index, word in enumerate(words):
        if len(words[index: index + n]) == n:
            ngram = tuple([word for word in words[index:index + n]])
            chains[ngram] = chains.get(ngram, [])
            # print ngram, "pass 3"
            try:
                words[index + n]
                # print words[index + n]
                chains[ngram].append(words[index + n])
            except IndexError:
                return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    for tuple_keys in chains.keys():
        if tuple_keys[0][0].isupper():
            current_tuple = tuple_keys
            break

    while True:
        # print current_tuple
        text += "{} ".format(current_tuple[0])
        if chains.get(current_tuple):
            next_word = choice(chains[current_tuple])  # might not exist might be empty list
            current_tuple = current_tuple[1:] + tuple([next_word])
        else:
            for tuple_word in current_tuple[1:]:
                text += "{} ".format(tuple_word)
            return text


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)
# print "Chains is: ", chains

# Produce random text
random_text = make_text(chains)

print random_text
