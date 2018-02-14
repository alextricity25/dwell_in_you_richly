# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
from diyr.engines.base import BaseEngineClass
import random

class FillInTheBlank(BaseEngineClass):

    def __init__(self, formatter, **kwargs):
        # kwargs desc:
        #    level = [0-9]+: How many words
        #    in the line to replace
        BaseEngineClass.__init__(self, formatter, **kwargs)
        self.n_replace_words = kwargs.get('level', 2)

    # run_engine processes the data on a per-line basis
    def run_engine(self):
        # The fill in the blank engine replaces some of words
        # that are in the body of the formatter's result with
        # underscores. The engine randomly selects words to
        # replace.
        for line in self.formatter.get_result():
            # Number of possible worlds in this line that can
            # can be replaced.
            # NOTE(alextricity25) For now, the possible number
            # of words the engine can replace will be the number
            # of all the words in a sentence. This will change
            # once we add the ability to exclude certain words.
            possible_rep_words = len(line['body'])
            # We want to preserve the line witout the replacements,
            # so we use a new list for the modified line
            new_line = list(line['body'])
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
                while random_index in replaced_indicies:
                    random_index = random.randint(0, upper_l)
                
                replaced_indicies.append(random_index)
                new_line[random_index] = (
                    "_" * len(line['body'][random_index]))
            # This engine modifies the dataset from the
            # formatter so that the body now returns a
            # tuple of the hollowed out line, and the
            # original.
            line['body'] = (line['body'], new_line)

            # Send the processed line to the caller
            yield line
