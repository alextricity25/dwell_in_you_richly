# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================


class BaseFormatClass():

    def __init__(self, stream):
        self.stream = stream

        # For each line of the input stream,
        # the formatter should include at
        # least the following data in the
        # result dict. This dict should be
        # populated in the get_result()
        # method
        self.result = {
            "body": object,
            "identifier": str,
            "extras": dict
        }

    # This function should return a generator yielding
    # the proper grammers formed by the respective format
    # type plugin. The grammers should parse the stream
    # input in a per-line basis.
    def get_result(self):
        pass
