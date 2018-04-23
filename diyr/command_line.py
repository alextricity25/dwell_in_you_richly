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
import difflib
import sys
import pdb

from diyr.utils.bible import Bible

class CommandLineRunner():

    def __init__(self, data, parsed_args):
        self.parsed_args = parsed_args
        self.data = data
        self.bible = Bible()
        self.num_correct = 0
        self.line_count = 0


    def run(self):
        for line in self.data:
            self.line_count += 1
            hollowed_verse = ' '.join(line['body'][1])
            verse = ' '.join(line['body'][0])
            identifier = line['identifier']
            expected_input = self._test_verse(hollowed_verse, identifier, verse, line)
            logging.debug("Expecting user input: {}".format(expected_input))
            if not self.parsed_args.generate:
                user_input = raw_input()
                if user_input.lower().strip() == expected_input:
                    print "Amen!"
                    self.num_correct += 1
                else:
                    d = difflib.Differ()
                    result = list(d.compare(
                        [user_input.lower() + '\n'],
                        [expected_input + '\n']))
                    print "Incorrect. Delta show below:"
                    print "-"*25
                    sys.stdout.writelines(result)
                    print "-"*25
                    if self.parsed_args.nail_it:
                        print "WRONG! NAIL IT MODE ENABLED!" + "-" * 15
                        for i in xrange(0,3):
                            expected_input = self._test_verse(hollowed_verse, identifier, verse, line)
                            user_input = raw_input()
                            if user_input.lower().strip() == expected_input:
                                print "\n"*100
                                print "YES!"
                                if i < 2: print "AGAIN!:"
                            else:
                                result = list(d.compare(
                                    [user_input.lower() + '\n'],
                                    [expected_input + '\n']))
                                print "\n"*100
                                print "NO! DELTA IS BELOW:"
                                sys.stdout.writelines(result)
                                if i < 2: print "TRY AGAIN:"
                        print "NAIL IT MODE COMPLETE. RESUMING AT NEXT LINE.." + "-" * 10

                # Score so far
                print "Score so far: {}/{}".format(
                    self.num_correct,
                    self.line_count)
            if (line['extras'].get('verse_references', '') and
            self.parsed_args.test_references and not
            self.parsed_args.generate):
                verses = ''.join(line['extras']['verse_references']).split(';')
                for verse in verses:
                    logging.debug("The raw verse from the engine is: {}".format(
                        verse))
                    print "Type the verse references verbatim:"
                    user_input_verse = raw_input()
                    ## The code below is logic written to handle different input
                    ## format from the user when inputting a verse reference.
                    ## The user can input a verse reference in it's abbrivated or
                    ## it's full form.
                    # Expected verse input
                    expected_verse_input = self.bible.extrapolate_abbriv(
                        verse,
                        raise_exp = False).lower().strip().replace(' ', '')
                    # Transformed user input.
                    # TODO: Extrapolate_abbriv cannot handle
                    # verse references that list verses in the
                    # same chapter that are not consecutive
                    # i.e. Acts 5:3-4, 8
                    trans_user_input = self.bible.extrapolate_abbriv(
                        user_input_verse,
                        raise_exp = False).lower().strip().replace(' ', '')
                    logging.debug("expected verse input: {}".format(
                        expected_verse_input))
                    logging.debug("transformed user input: {}".format(
                        trans_user_input))
                    if expected_verse_input == trans_user_input:
                        print "Amen!"
                    else:
                        print "Wrong. The verse reference is: {}".format(verse)

    def _test_verse(self, hollowed_verse, identifier, verse, line):
        identifier_prop = line['extras'].get("identifier_position", '')
        if identifier_prop == 'after':
            print "{} - {}".format(hollowed_verse, identifier)
            return "{} - {}".format(verse, identifier).lower().strip()
        elif identifier_prop == 'off':
            print hollowed_verse
            return verse.lower().strip()
        else:
            print "{}{}".format(identifier, hollowed_verse)
            return "{}{}".format(identifier, verse).lower().strip()
