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
import logging

class OnlineSourceClass(BaseSourceClass):

    def __init__(self, url = "", book = "", chapter = ""):
        logging.debug("Initializing OnlineSourceClass...")
        self.bible_utils = Bible()
        self.BIBLE = self.bible_utils.BIBLE
        self.book = book
        self.chapter = chapter
        BaseSourceClass.__init__(self, source = url)
        logging.debug("Pulling {} {} from {}".format(
            book,
            chapter,
            self.source))

    def get_stream(self):
        retries = 0
        status_code = 0
        while retries < 5:
            logging.debug("Number of retries: {}".format(retries))

            # If book and chapter are given, then simply set the
            # ``book_name`` and ``chapter_number`` variables to
            # what was given, else, randomize them.
            if self.book and self.chapter:
                book_number = self._get_book_num(self.book)
                book_name = self.book
                chapter_number = self.chapter
            else:
                # Randomize the book
                #TODO: There is an easier way to pick a random element
                # from an array using the random library
                book_number = random.randint(1, len(self.BIBLE.keys()))
                book_name = list(self.BIBLE.keys())[book_number]
                chapter_number = random.randint(1, int(self.BIBLE[book_name]['chapters']))

            try:
                verses_list = self.bible_utils.get_online_chapter(book_name, chapter_number)
                break
            except Exception as e:
                logging.info("Exception from get_online_chapter")
                logging.info(e.message)
                retries += 1
                continue

        print "The book {} chapter {} will be used".format(
            book_name,
            chapter_number)

        # If max retires was hit, throw an error
        if retries >= 5:
            logging.warn("The maximum amount of retires has been exceeded!")
            raise Exception("Cloud not find book and chapter! Please try again!")
        return verses_list

    def _remove_non_ascii(self, text):
        return ''.join(i for i in text if ord(i)<128)

    def _get_book_num(self, book):
        # Adding one because lists are indexed starting
        # with zero.
        return self.BIBLE.keys().index(book)
