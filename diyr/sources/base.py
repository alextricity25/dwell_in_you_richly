# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

class BaseSourceClass():

    def __init__(self, **kwargs):
        # Source can be a file path or a url.
        # (alextricity25) Any other sources?
        self.source = kwargs['source']


    def get_stream(self):
        pass
