# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import random
import logging

from diyr.engines.base import BaseEngineClass

class FillInTheBlank(BaseEngineClass):

    def __init__(self, formatter, **kwargs):
        # kwargs desc:
        #    level = [0-9]+: How many words
        #    in the line to replace

        self.excluded_words = [
            "also",
            "an",
            "and",
            "another",
            "any",
            "are",
            "as",
            "at",
            "be",
            "because",
            "been",
            "being",
            "both",
            "but",
            "by",
            "came",
            "can",
            "did",
            "do",
            "each",
            "for",
            "has",
            "had",
            "he",
            "have",
            "her",
            "here",
            "him",
            "himself",
            "his",
            "how",
            "if",
            "in",
            "into",
            "is",
            "it",
            "like",
            "make",
            "me",
            "might",
            "much",
            "my",
            "of",
            "on",
            "or",
            "our",
            "out",
            "over",
            "said",
            "should",
            "since",
            "some",
            "still",
            "such",
            "take",
            "than",
            "that",
            "the",
            "their",
            "them",
            "then",
            "there",
            "these",
            "they",
            "this",
            "those",
            "to",
            "too",
            "very",
            "was",
            "way",
            "we",
            "well",
            "were",
            "what",
            "where",
            "which",
            "while",
            "who",
            "with",
            "would",
            "you",
            "your",
        ]
        BaseEngineClass.__init__(self, formatter, **kwargs)
        logging.debug("Initializing FillInTheBlank...")
        self.n_replace_words = kwargs.get('level', 2)
        logging.debug(("This engine will attempt to replace " +
                       "{} words with underscores".format(
                           self.n_replace_words)))

    # run_engine processes the data on a per-line basis
    def run_engine(self):
        # The fill in the blank engine replaces some of words
        # that are in the body of the formatter's result with
        # underscores. The engine randomly selects words to
        # replace.
        for line in self.formatter.get_result():
            # Number of possible worlds in this line that can
            # can be replaced.
            # The number of negative words that exist in the
            # line need to be counted so that we know how many to exclude
            # from the number of possible words that can be excluded.
            negatives = 0
            for word in line['body']:
                if word.lower() in self.excluded_words:
                    negatives += 1

            possible_rep_words = len(line['body']) - negatives
            logging.debug(("Number of words that can be possibly " +
                           "replaced: {}".format(possible_rep_words)))
            # We want to preserve the line witout the replacements,
            # so we use a new list for the modified line
            new_line = list(line['body'])
            logging.debug("The line that is being processed: {}".format(
                new_line))
            # Subtract one because lists are indexed starting
            # from zero
            upper_l = len(line['body']) - 1
            replaced_indicies = []
            # If the number of user-defined words to replace is greater
            # than the number of possible words to replace,
            # then just replace all of the words possible.
            if self.n_replace_words > possible_rep_words:
                words_to_replace = possible_rep_words
            else:
                words_to_replace = self.n_replace_words
            logging.debug(("The number of words that are going to be " +
                           "actually replaced are: {}".format(
                               words_to_replace)))
            for i in xrange(words_to_replace):
                # Generate random index
                random_index = random.randint(0, upper_l)
                # This condition is put in place so the same
                # word is not replaced twice
                # If the index has already been replaced,
                # then generate a new one. We keep doing
                # this until either the number of possible
                # words to replace is exceeded, or
                # n_replace_word is exceeded.
                logging.debug("Attempting to replace the word: {}".format(
                    new_line[random_index]))
                while random_index in replaced_indicies or new_line[random_index] in self.excluded_words:
                    logging.debug(("This word has already been replaced or is a negative. " +
                                   "Randomizing again..."))
                    random_index = random.randint(0, upper_l)
                
                replaced_indicies.append(random_index)
                logging.debug("The word that is being replaced is: {}".format(
                    new_line[random_index]))
                new_line[random_index] = (
                    "_" * len(line['body'][random_index]))
            # This engine modifies the dataset from the
            # formatter so that the body now returns a
            # tuple of the hollowed out line, and the
            # original.
            line['body'] = (line['body'], new_line)
            logging.debug("The replaced word is {}".format(line['body']))

            # Send the processed line to the caller
            yield line
