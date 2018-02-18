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
from diyr.sources.base import BaseSourceClass

class FileSourceClass(BaseSourceClass):

    def __init__(self, file_path=""):
        logging.debug("Initializing FileSourceClass...")
        BaseSourceClass.__init__(self, source = file_path)
        # self.source should now be avialable to this instance
        # and containing the file path of the file to be read

    def get_stream(self):
        logging.debug("Reading from file: {}".format(self.source))
        return open(self.source, 'r')
