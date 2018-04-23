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

from diyr.sinks.base import BaseSinkClass

class NothingSink(BaseSinkClass):

    def __init__(self, engine, **kwargs):
        """
        This sink leaves the data untouched.
        """
        logging.debug("Initializing NothingSink Class...") 
        BaseSinkClass.__init__(self, engine, **kwargs)
        
    def process(self):

        return self._collect_data()
