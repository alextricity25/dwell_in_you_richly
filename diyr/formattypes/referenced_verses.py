# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from pyparsing import Word, alphas, OneOrMore, nums, Group, Suppress, Optional
from diyr.formattypes.base import BaseFormatClass

class ReferencedVerses(BaseFormatClass):

    def __init__(self, stream):
    
        BaseFormatClass.__init__(self, stream)
        # Grammers defined here
        #NOTE: self.verse_word is defined in the base class
        #NOTE: self.verse is defined in the base class
        self.book_num = Optional(Word(nums, exact = 1))
        self.book_name = Word(alphas)
        self.book_chapter = Word(nums)
        self.book_verse = Word(nums) 
        self.reference = (self.book_num +
                          self.book_name +
                          self.book_chapter + ":" + self.book_verse)
        # This is the dataset we will mainly be operating on, since
        # it will contain the verse and the reference seperated out
        self.verse_reference = Group(self.verse) + Suppress('-') + Group(self.reference)


    # Must return a dataset with these 
    def get_result(self):
        # Reading input stream line by line
        for line in self.stream:
            parsed_line = self.verse_reference.parseString(line)
            self.result['body'] = parsed_line[0]
            # The identifier for each line when this file format is used
            # is the verse reference
            self.result['identifier'] = parsed_line[1]
            # There are no extras for this formatter
            self.result['extras'] = None
            yield self.result
