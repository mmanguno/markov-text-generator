# Copyright Mitchell Manguno 2016
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
A simple text generator based on Markov chains.
"""
__author__ = "Mitchell Manguno"
__version__ = "0.3"
__date__ = "11 July 2016"

from argparse import ArgumentParser
from random import choice
from string import punctuation


# Handle some python2 and python compatability; use xrange as signal
try:
    xrange  # Python3 doesn't have xrange; this'll throw a NameError

    def _strip_punct(word): return word.translate(None, punctuation)

except NameError:
    xrange = range  # Set xrange to range; also, account for translate function
    trans_table = {ord(c): None for c in punctuation}

    def _strip_punct(word): return word.translate(trans_table)


def _read(in_file, lowercase, punct):
    """Reads in a file and turns it into a list of words.

    Parsing from a list of words, while it takes more memory, is just
    easier to deal with later on. So do that here.

    Keyword arguments:
    in_file -- the input file to pull the text from
    lowercase -- boolean determining if all words are forced to all lowercase
    punct -- boolean determining if punctuation is stripped or not
    Returns a list of all words in the text
    """
    words = []
    with open(in_file, 'r') as f:
        for line in f:
            for word in line.split():
                transformed_word = word
                if not punct:  # strips punctuation
                    transformed_word = _strip_punct(word)
                if lowercase:  # force to lowercase
                    transformed_word = str.lower(transformed_word)
                words.append(transformed_word)
    return words


def _parse(words):
    """Parses a list of words into a dictionary of dictionaries.

    For each word, we look at the possible next-words, and count the number
    of times that they appear. So if a phrase is "The house, the room", the
    parsed value is
        {the : {house : 1, room: 1}, house : {the : 1}, room : {the : 1}}.
    Words that only appear at the end of the phrase will have their successor
    set to the first word in the text.

    Keyword arguments
    words -- a list of all the words in the text
    Returns a dictionary of dictionaries of words and their successors
    """
    word_successors = {}  # For each word, put its successors in here
    for x in xrange(len(words) - 1):
        cur = words[x]
        nex = words[x + 1]
        if cur not in word_successors.keys():
            word_successors[cur] = {nex: 1}
        else:
            if nex not in word_successors[cur].keys():
                word_successors[cur][nex] = 1
            else:
                word_successors[cur][nex] = word_successors[cur][nex] + 1

    # if the last word appears only at the end, add it
    if words[len(words) - 1] not in word_successors.keys():
        word_successors[words[len(words) - 1]] = {words[0]: 1}
    return word_successors


def _generate_text(word_successors, length):
    """Generates text with the Markov assumption.

    Generates some text corresponding to a dictionary of dictionaries of words
    and their successors. Chooses next words according to the number of times
    a next value appears.

    Keyword arguments:
    word_successors -- dictionary of dictionaries of words and their successors
    length -- the length of the generated text
    Returns the generated text as a list of words.
    """
    generated = []
    # Randomly choose a word to start with
    start_word = choice(list(word_successors))
    generated.append(start_word)
    for x in xrange(1, length):
        cur = generated[x - 1]
        candidates = word_successors[cur]  # The dictionary of candidates
        # Use choice on a list where keys appear as many times as their value
        nex = choice([x for x in candidates for k in range(0, candidates[x])])
        generated.append(nex)

    return generated


def _format_generated_text(generated_text):
    """Formats the text into something that looks like a sentence.

    Joins the words from the list of generated text together. Capitalizes
    the first word, and puts a period on the last word.

    Keyword arguments:
    generated_text -- the text to format
    Returns a 'sentence-like' string of words.
    """
    sentence = ' '.join(generated_text)
    first_char = str.upper(sentence[0])
    new_sentence = sentence[1:]

    return first_char + new_sentence + '.'


def run(in_file, length, lowercase, punct):
    """Runs the whole process to provide some generated text of a given length

    Runs the read, parse, generate_text, and format_generated_text in sequence
    to produce the whole effect of the text generator.

    Keyword arguments:
    in_file -- the file to read and generate text from
    length -- the lenght of the output generated text
    lowercase -- boolean determining if all words are forced to all lowercase
    punct -- boolean determining if punctuation is stripped or not
    Returns text generated by the Markov text generator
    """
    words = _read(in_file, lowercase, punct)
    word_dict = _parse(words)
    text = _generate_text(word_dict, length)
    return _format_generated_text(text)


def main():
    parser = ArgumentParser(description='Generates text using a Markov' +
                            ' text generator.')
    parser.add_argument('in_file', metavar='file', type=str, nargs='+',
                        help='the file to read in as source')
    parser.add_argument('--length', metavar='length', type=int, nargs='?',
                        default=100,
                        help='the length of text to output')
    parser.add_argument('--lower', metavar='lower', type=str, nargs='?',
                        default='False',
                        help='y/yes/true: force all words to lowercase')
    parser.add_argument('--punct', metavar='punct', type=str, nargs='?',
                        default='True',
                        help='y/yes/true: strip punctuation from input file')

    args = parser.parse_args()
    in_file = args.in_file[0]
    length = args.length
    lower = str.lower(args.lower) in ['y', 'yes', 'true']
    punct = str.lower(args.punct) in ['y', 'yes', 'true']

    print(run(in_file, length, lower, punct))

if __name__ == '__main__':
    main()
