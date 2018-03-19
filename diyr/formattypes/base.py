# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

import logging
from pyparsing import Word, alphas, OneOrMore, nums, Group, Optional

class BaseFormatClass():

    def __init__(self, stream):
        logging.debug("Initializing BaseFormatClass...")
        self.stream = stream

        # For each line of the input stream,
        # the formatter should include at
        # least the following data in the
        # result dict. This dict should be
        # populated in the get_result()
        # method
        self.result = {
            "body": object,
            "identifier": str,
            "extras": dict
        }

        # These are some common pyparsing objects that
        # the formatter drivers can use.
        # Each word in a verse can be composed of any letter
        # in the english alphabet, plus grammer characters.
        bible_grammer_chars = '.,?;!\'/()'
        # A dashed word is a token with more then just 2 characters.
        # The minimum restrictions is placed so that only dashes
        # are not matched as words in a string literal
        dashed_word = Word(alphas + bible_grammer_chars + "-", min = 2)
        self.verse_word = Word(alphas + bible_grammer_chars) ^ dashed_word
        self.verse = OneOrMore(self.verse_word)

        logging.debug("Stream line is: {}".format(self.stream))

    # This function should return a generator yielding
    # the proper grammers formed by the respective format
    # type plugin. The grammers should parse the stream
    # input in a per-line basis.
    def get_result(self):
        pass
