import sys
from random import choice

def open_and_read_file(filepath):
    """ Takes a string that is a filepath, opens the file, reads
        the text and returns one long string"""

    file = open(filepath)
    text = file.read()
    file.close()

    return text


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains."""

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

    key = choice([key for key in chains.keys() if key[0][0].isupper()])
    words = list(key)
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        try:
            word = choice(chains[key])
            words.append(word)
            key = key[1:] + tuple([word])
        except IndexError:
            break
        if key[-1][-1] in ".?;!":
            break

    return " ".join(words)

# Get the filepath from the user through a command line prompt, ex:
    # python markov.py green-eggs.txt

input_path = sys.argv[1]

    # This could also say something like:
    #   input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains)

print random_text
