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

class CommandLineRunner():

    def __init__(self, engine, parsed_args):
        self.parsed_args = parsed_args
        self.engine = engine


    def run(self):
        for line in self.engine.run_engine():
            hollowed_verse = ' '.join(line['body'][1])
            verse = ' '.join(line['body'][0])
            identifier = line['identifier']
            if line['extras'].get("identifier_position", '') == 'after':
                expected_input = "{} {}".format(
                    verse,
                    identifier).lower().strip()
                print "{} {}".format(hollowed_verse, identifier)
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
                print "Incorrect."

            if line['extras'].get('verse_references', '') and self.parsed_args.test_references:
                verses = ''.join(line['extras']['verse_references']).split(';')
                for verse in verses:
                    print "Type the verse references verbatim:"
                    user_input_verse = raw_input()
                    if user_input_verse.lower().strip() == verse.lower().strip():
                        print "Amen!"
                    else:
                        print "Wrong. The verse reference is: {}".format(verse)
