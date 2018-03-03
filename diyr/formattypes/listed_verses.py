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

from pyparsing import Word, alphas, OneOrMore, nums, Group
from diyr.formattypes.base import BaseFormatClass

class ListedVerses(BaseFormatClass):

    def __init__(self, stream):

        BaseFormatClass.__init__(self, stream)
        logging.debug("Initializing ListedVerses...")
        # NOTE: self.verse_word is defined in the base class
        # NOTE: self.verse is defined in the base class
        # Grammers defined here
        # The verses for this formatter are listed numerically
        # The identifier this formatter will use the number.
        self.number = Word(nums + ".")
        # This is the dataset we will mainly be operating on, since
        # it will contain the verse and the identifier
        self.verse_reference = Group(self.number) + Group(self.verse)


    # Must return a dataset with these 
    def get_result(self):
        # Reading input stream line by line
        for line in self.stream:
            logging.debug("Parsing line {}".format(line))
            parsed_line = self.verse_reference.parseString(line)
            self.result['body'] = parsed_line[1]
            logging.debug("Body for this line is: {}".format(
                self.result['body']))
            # The identifier for each line when this file format is used
            # is the prepended number (The verse number)
            self.result['identifier'] = ''.join(parsed_line[0])
            logging.debug("Identifier for this line is {}".format(
                self.result['identifier']))
            # There are no extras for this formatter
            self.result['extras'] = {}
            yield self.result
