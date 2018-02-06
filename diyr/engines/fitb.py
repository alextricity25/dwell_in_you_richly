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
            #print line['body'].join(' ')
            new_line = list(line['body'])
            # Subtract one because lists are indexed starting
            # from zero
            upper_l = len(line['body']) - 1
            replaced_indicies = []
            for i in xrange(self.n_replace_words):
                # Generate random index
                random_index = random.randint(0, upper_l)
                # This condition is put in place so the same
                # word is not replaced twice
                # If the index has already been replaced,
                # then generate a new one.
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

            yield line
