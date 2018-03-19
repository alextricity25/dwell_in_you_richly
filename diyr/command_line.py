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

    def __init__(self, engine, parsed_args):
        self.parsed_args = parsed_args
        self.engine = engine
        self.bible = Bible()


    def run(self):
        for line in self.engine.run_engine():
            hollowed_verse = ' '.join(line['body'][1])
            verse = ' '.join(line['body'][0])
            identifier = line['identifier']
            if line['extras'].get("identifier_position", '') == 'after':
                expected_input = "{} - {}".format(
                    verse,
                    identifier).lower().strip()
                print "{} - {}".format(hollowed_verse, identifier)
            elif line['extras'].get("identifier_position", '') == 'off':
                expected_input = verse.lower().strip()
                print hollowed_verse
            else:
                expected_input = "{}{}".format(
                    identifier,
                    verse).lower().strip()
                print "{}{}".format(identifier, hollowed_verse)
            logging.debug("Expecting user input: {}".format(expected_input))
            user_input = raw_input()
            if user_input.lower().strip() == expected_input:
                print "Amen!"
            else:
                d = difflib.Differ()
                result = list(d.compare(
                    [user_input.lower() + '\n'],
                    [expected_input + '\n']))
                print "Incorrect. Delta show below:"
                sys.stdout.writelines(result)

            if line['extras'].get('verse_references', '') and self.parsed_args.test_references:
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
