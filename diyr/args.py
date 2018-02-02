# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================


import argparse
import os

example_file_path  = (os.path.dirname(os.path.realpath(__file__)) +
"//example_format_types/listed_verses.txt")

parser = argparse.ArgumentParser(
    usage = '%(prog)s',
    description = 'A tool to help you let the Word of Christ dwell in' \
                  'you richly'
)

parser.add_argument(
    '-f',
    '--file',
    help = 'The file of a correct format type to hollow',
    required = False,
    default = example_file_path
)

parser.add_argument(
    '-t',
    '--type',
    help = 'The format type of the provided file.',
    choices = [
        'listed_verses',
        'referenced_verses',
        'outline'
    ],
    default = 'listed_verses',
    required = False
)

parser.add_argument(
    '-m',
    '--mode',
    help = "The mode of the game, which will determine the engine.",
    choices = [
        'fitb'
    ],
    default = 'fitb',
    required = False
)

def get_parser():
    return parser
