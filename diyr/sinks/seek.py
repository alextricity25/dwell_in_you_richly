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
import re

from diyr.sinks.base import BaseSinkClass

class SeekSinkClass(BaseSinkClass):

    def __init__(self, engine, **kwargs):
        logging.debug("Initializing SeekSinkClass...")
        BaseSinkClass.__init__(self, engine, **kwargs)
        self.pattern = kwargs['pattern']

    def _collect_data_from_pattern(self):
        all_data = []
        add = False
        reg = re.compile(self.pattern)
        for line in self.engine.run_engine():
            if reg.search(' '.join(line['body'][0])) or add:
                add = True
                logging.debug("Adding {} to all_data".format(line))
                all_data.append(line.copy())
        return all_data

    def process(self):
        #self._iterate_until_match()
        return self._collect_data_from_pattern()
