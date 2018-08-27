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

        """
	This function returns the generator produced by the engine. Since there
        is nothing to do here, there is no need to collect *all* the data that
        the engine produces at once. We can just allow the engine to return the
        data iteratively.
        """
        return self.engine.run_engine()
