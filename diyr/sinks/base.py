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
import pdb

from diyr.engines.base import BaseEngineClass

class BaseSinkClass():

    def __init__(self, engine, **kwargs):
        logging.debug("Initializing BaseSinkClass...")
        if not isinstance(engine, BaseEngineClass):
            raise Exception('Sink class must be initialized with an egine object!')
        self.engine = engine

    def _collect_data(self):
        """
        Returns a list of all the data gathered from the engine
        iterable.
        """
        all_data = []
        for line in self.engine.run_engine():
            logging.debug("Adding {} to all_data".format(line))
            all_data.append(line.copy())
            logging.debug("all_data is now {}".format(all_data))

        return all_data
