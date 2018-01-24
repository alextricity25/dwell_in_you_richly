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

parser = argparse.ArgumentParser(
    usage = '%(prog)s',
    description = 'A tool to help you let the Word of Christ dwell in' \
                  'you richly'
)

parser.add_argument(
    '-f',
    '--file',
    help = 'The file of a correct format type to hollow',
    required = True
)

parser.add_argument(
    '-t',
    '--type',
    help = 'The format type of the provided file.',
    choices = [
        'listed_verses',
        'referenced_verse',
        'outline'
    ],
    required = True
)

def get_parser():
    return parser
