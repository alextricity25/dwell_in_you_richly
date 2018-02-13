# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from pyparsing import Word, alphas, OneOrMore, nums, Group
from diyr.formattypes.base import BaseFormatClass

class ListedVerses(BaseFormatClass):

    def __init__(self, stream):
    
        # Grammers defined here
        self.verse_word = Word( alphas + '.,?;!\'/')
        self.verse = OneOrMore(self.verse_word)
        # The verses for this formatter are listed numerically
        # The identifier this formatter will use the number.
        self.number = Word(nums + ".")
        # This is the dataset we will mainly be operating on, since
        # it will contain the verse and the identifier
        self.verse_reference = Group(self.number) + Group(self.verse)
        BaseFormatClass.__init__(self, stream)


    # Must return a dataset with these 
    def get_result(self):
        # Reading input stream line by line
        for line in self.stream:
            parsed_line = self.verse_reference.parseString(line)
            self.result['body'] = parsed_line[1]
            # The identifier for each line when this file format is used
            # is the prepended number (The verse number)
            self.result['identifier'] = parsed_line[0]
            # There are no extras for this formatter
            self.result['extras'] = None
            yield self.result
