#!/user/bin/env python
# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from diyr import args
from diyr import formattypes


def main():
    dir(args)
    parsed_args = args.get_parser().parse_args()


if __name__ == "__main__":
    main()
