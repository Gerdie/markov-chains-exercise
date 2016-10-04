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

def make_chains(text_string):
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
        if words[index + 1]:
            bigram = (word, words[index+1])
            chains[bigram] = chains.get(bigram, [])
            try:
                words[index + 2]
                chains[bigram].append(words[index + 2])
            except IndexError:
                return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    current_tuple = choice(chains.keys())

    while True:
        text += "{} ".format(current_tuple[0])
        if chains.get(current_tuple):
            next_word = choice(chains[current_tuple])  # might not exist might be empty list
            current_tuple = (current_tuple[1], next_word)
        else:
            text += "{} ".format(current_tuple[1])
            return text


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
#print chains

# Produce random text
random_text = make_text(chains)

print random_text
