# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from diyr.formattypes.base import BaseFormatClass

class BaseEngineClass():

    def __init__(self, formatter, **kwargs):

        if not isinstance(formatter, BaseFormatClass):
             raise Exception('Engine class must be initialized with a formatter!')
        self.formatter = formatter

    # The meat of it all
    def run_engine():
        pass
