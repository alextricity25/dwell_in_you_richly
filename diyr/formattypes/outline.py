# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from pyparsing import Word, alphas, OneOrMore, nums, Group, Optional, ZeroOrMore
from diyr.formattypes.base import BaseFormatClass
import pdb

class Outline(BaseFormatClass):

    def __init__(self, stream):
        BaseFormatClass.__init__(self, stream)
        # Grammers defined here
        self.roman_letters = "IVX"
        self.roman_letters_small = 'ivx'
        self.points = OneOrMore(Word(self.roman_letters +
                                     alphas +
                                     nums +
                                     self.roman_letters_small))
        self.point_identifier = self.points + "."

        self.chapter_and_verse = Word(nums) + \
                                 ":" + \
                                 Word(nums) + \
                                 Optional("-") + \
                                 Optional(Word(nums)) + \
                                 Optional(Word(";,"))
        self.listed_verse_grammer = Word(nums) + Optional(Word(";,"))
        self.abbriv = Word(alphas + ".")
        self.verse_list = OneOrMore(
                              self.listed_verse_grammer ^
                              self.chapter_and_verse)
        self.verses = self.abbriv + self.verse_list
        
        # Grammer to match the line on an outline
        self.line_grammer = Group(Optional(self.point_identifier)) + \
                            Group(self.verse) + \
                            Optional("-") + \
                            Group(ZeroOrMore(self.verses))

    def get_result(self):
        for line in self.stream:
            parsed_line = self.line_grammer.parseString(line)
            #pdb.set_trace()
            self.result['body'] = parsed_line[1]
            # The identifier for each line when this file format is
            # used is the point identifier
            self.result['identifier'] = parsed_line[0]
            self.result['extras'] = {
                'verse_references': parsed_line[-1] }
            yield self.result
