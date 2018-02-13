# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

from bs4 import BeautifulSoup
from diyr.sources.base import BaseSourceClass
from diyr.utils.bible import Bible

import requests
import random
import re

class OnlineSourceClass(BaseSourceClass):

    def __init__(self, url = ""):
        self.BIBLE = Bible().BIBLE
        BaseSourceClass.__init__(self, source = url)

    def get_stream(self):
        retries = 0
        status_code = 0
        while status_code != 200 and retries < 5:
            # Randomize the book
            # Take note of the one-off number due to indicies starting at zero
            book_number = random.randint(1, len(self.BIBLE.keys()))
            book_name = list(self.BIBLE.keys())[book_number]
            chapter_number = random.randint(1, int(self.BIBLE[book_name]['chapters']))
            # This is the URL that online.recoveryversion
            # uses for the text based version of the Bible.
            url = "{}/{}_{}{}.htm".format(
                      self.source,
                      book_number + 1,
                      # Spaces are removed to deal with
                      # book names that include a number.
                      # i.e. "1 Corinthians"
                      book_name.replace(" ", ""),
                      chapter_number)
            r = requests.get(url)
            status_code = r.status_code

            # If status_code is not 201, there is no
            # need to continue with this iteration.
            # Instead, we are going to randomize the
            # bible again and retry the request.
            if status_code != 200:
                retries += 1
                continue

            chapter_html = r.text
            soup = BeautifulSoup(chapter_html, 'html.parser')
            verses_list_soup = soup.get_text().split('\n')
            # Clean up verses list
            # This is being done because some non alphanumeric
            # ASCII characters might have been picked up from the
            # web scraper
            verses_list = []
            verse_num = 1
            for verse in verses_list_soup:
                verse = self._remove_non_ascii(verse)
                if re.search(r'[0-9]+:[0-9]+', verse):
                    verses_list.append(
                         re.sub(r'[0-9]+:[0-9]+',
                                str(verse_num) + ".",
                                verse))
                verse_num += 1
        print "The book {} chapter {} was chosen for you!".format(
            book_name,
            chapter_number)
        return verses_list

    def _remove_non_ascii(self, text):
        return ''.join(i for i in text if ord(i)<128)
