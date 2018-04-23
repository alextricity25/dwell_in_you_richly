# =============================================================================
# Copyright [2018] [Miguel Alex Cantu]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import re
import requests
import logging
from collections import OrderedDict
from bs4 import BeautifulSoup

class Bible():

    def __init__(self):
        self.BIBLE = OrderedDict()
        self.BIBLE['Genesis'] = {'chapters': 50, 'abbriv': 'Gen.'}
        self.BIBLE['Exodus'] = {'chapters': 40, 'abbriv': 'Exo.'}
        self.BIBLE['Leviticus'] = {'chapters': 27, 'abbriv': 'Lev.'}
        self.BIBLE['Numbers'] = {'chapters': 36, 'abbriv': 'Num.'}
        self.BIBLE['Deuteronomy'] = {'chapters': 34, 'abbriv': 'Deut.'}
        self.BIBLE['Joshua'] = {'chapters': 24, 'abbriv': 'Josh.'}
        self.BIBLE['Judges'] = {'chapters': 21, 'abbriv': 'Jud.'}
        self.BIBLE['Ruth'] = {'chapters': 4, 'abbriv': 'Ruth'}
        self.BIBLE['1 Samuel'] = {'chapters': 31, 'abbriv': '1 Sam.'}
        self.BIBLE['2 Samuel'] = {'chapters': 24, 'abbriv': '2 Sam.'}
        self.BIBLE['1 Kings'] = {'chapters': 22, 'abbriv': '1 Kings'}
        self.BIBLE['2 Kings'] = {'chapters': 25, 'abbriv': '2 Kings'}
        self.BIBLE['1 Chronicles'] = {'chapters': 29, 'abbriv': '1 Chron.'}
        self.BIBLE['2 Chronicles'] = {'chapters': 36, 'abbriv': '2 Chron.'}
        self.BIBLE['Ezra'] = {'chapters': 10, 'abbriv': 'Ezra'}
        self.BIBLE['Nehemiah'] = {'chapters': 13, 'abbriv': 'Neh.'}
        self.BIBLE['Esther'] = {'chapters': 10, 'abbriv': 'Esther'}
        self.BIBLE['Job'] = {'chapters': 42, 'abbriv': 'Job'}
        self.BIBLE['Psalms'] = {'chapters': 150, 'abbriv': 'Ps.'}
        self.BIBLE['Proverbs'] = {'chapters': 31, 'abbriv': 'Prov.'}
        self.BIBLE['Ecclesiastes'] = {'chapters': 12, 'abbriv': 'Eccl.'}
        self.BIBLE['Song of Solomon'] = {'chapters': 8, 'abbriv': 'S.s.'}
        self.BIBLE['Isaiah'] = {'chapters': 66, 'abbriv': 'Isa.'}
        self.BIBLE['Jeremiah'] = {'chapters': 52, 'abbriv': 'Jer.'}
        self.BIBLE['Lamentations'] = {'chapters': 5, 'abbriv': 'Lam.'}
        self.BIBLE['Ezekiel'] = {'chapters': 48, 'abbriv': 'Ezek.'}
        self.BIBLE['Daniel'] = {'chapters': 12, 'abbriv': 'Dan.'}
        self.BIBLE['Hosea'] = {'chapters': 14, 'abbriv': 'Hos.'}
        self.BIBLE['Joel'] = {'chapters': 3, 'abbriv': 'Joel'}
        self.BIBLE['Amos'] = {'chapters': 9, 'abbriv': 'Amos'}
        self.BIBLE['Obadiah'] = {'chapters': 1, 'abbriv': 'Obad.'}
        self.BIBLE['Jonah'] = {'chapters': 4, 'abbriv': 'Jonah'}
        self.BIBLE['Micah'] = {'chapters': 7, 'abbriv': 'Micah'}
        self.BIBLE['Nahum'] = {'chapters': 3, 'abbriv': 'Nahum'}
        self.BIBLE['Habakkuk'] = {'chapters': 3, 'abbriv': 'Hab.'}
        self.BIBLE['Zephaniah'] = {'chapters': 3, 'abbriv': 'Zep.'}
        self.BIBLE['Haggai'] = {'chapters': 2, 'abbriv': 'Hag.'}
        self.BIBLE['Zechariah'] = {'chapters': 14, 'abbriv': 'Zech.'}
        self.BIBLE['Malachi'] = {'chapters': 4, 'abbriv': 'Mal.'}
        self.BIBLE['Matthew'] = {'chapters': 28, 'abbriv': 'Matt.'}
        self.BIBLE['Mark'] = {'chapters': 16, 'abbriv': 'Mark'}
        self.BIBLE['Luke'] = {'chapters': 24, 'abbriv': 'Luke'}
        self.BIBLE['John'] = {'chapters': 21, 'abbriv': 'John'}
        self.BIBLE['Acts'] = {'chapters': 28, 'abbriv': 'Acts'}
        self.BIBLE['Romans'] = {'chapters': 16, 'abbriv': 'Rom.'}
        self.BIBLE['1 Corinthians'] = {'chapters': 16, 'abbriv': '1 Corin.'}
        self.BIBLE['2 Corinthians'] = {'chapters': 13, 'abbriv': '2 Corin.'}
        self.BIBLE['Galatians'] = {'chapters': 6, 'abbriv': 'Gal.'}
        self.BIBLE['Ephesians'] = {'chapters': 6, 'abbriv': 'Eph.'}
        self.BIBLE['Philippians'] = {'chapters': 4, 'abbriv': 'Phil.'}
        self.BIBLE['Colossians'] = {'chapters': 4, 'abbriv': 'Col.'}
        self.BIBLE['1 Thessalonians'] = {'chapters': 5, 'abbriv': '1 Thes.'}
        self.BIBLE['2 Thessalonians'] = {'chapters': 3, 'abbriv': '2 Thes.'}
        self.BIBLE['1 Timothy'] = {'chapters': 6, 'abbriv': '1 Tim.'}
        self.BIBLE['2 Timothy'] = {'chapters': 4, 'abbriv': '2 Tim.'}
        self.BIBLE['Titus'] = {'chapters': 3, 'abbriv': 'Titus'}
        self.BIBLE['Philemon'] = {'chapters': 1, 'abbriv': 'Philemon'}
        self.BIBLE['Hebrews'] = {'chapters': 13, 'abbriv': 'Heb.'}
        self.BIBLE['James'] = {'chapters': 5, 'abbriv': 'James'}
        self.BIBLE['1 Peter'] = {'chapters': 5, 'abbriv': '1 Pet.'}
        self.BIBLE['2 Peter'] = {'chapters': 3, 'abbriv': '2 Pet.'}
        self.BIBLE['1 John'] = {'chapters': 5, 'abbriv': '1 John'}
        self.BIBLE['2 John'] = {'chapters': 1, 'abbriv': '2 John'}
        self.BIBLE['3 John'] = {'chapters': 1, 'abbriv': '3 John'}
        self.BIBLE['Jude'] = {'chapters': 1, 'abbriv': 'Jude'}
        self.BIBLE['Revelation'] = {'chapters': 22, 'abbriv': 'Rev.'}

    def extrapolate_abbriv(self, verse, raise_exp = True):
        reg = re.compile('(([0-9]*) *[\D]+) *([-0-9:,]*)')
        m = reg.match(verse)
        book_name_abbriv = m.group(1).strip()
        for book, prop in self.BIBLE.iteritems():
            if (prop['abbriv'].lower().replace('.','').replace(' ', '') ==
                book_name_abbriv.lower().replace('.', '').replace(' ', '')):
                return "{} {}".format(
                    book,
                    m.group(3)).strip()
        if raise_exp:
            raise Exception("Abbriviation did not match book")
        else:
            return verse

    def return_abbriv(self, book):
        return self.BIBLE[book]['abbriv']

    def build_recovery_online_url(self, book_name, book_chapter):
        """
        Returns a string composing the url of the online.recoveryversion.bible
        of the given book name and chapter
        TODO: Write notes here about how that URL is composed, and what is expected
        by online.recoveryversion.bible
        """
        base_url = "http://online.recoveryversion.bible/txo"
        return "{}/{}_{}{}.htm".format(
                                base_url,
                                self.get_book_number(book_name),
                                # Spaces are removed to deal with book names
                                # that include a number. i.e. 1 Corinthians
                                book_name.replace(" ", ""),
                                book_chapter)

    def get_online_chapter(self, book_name, book_chapter):
        """
        Retrieves an entire chapter of a book in the Bible in the form of a
        list
        """
        url = self.build_recovery_online_url(book_name, book_chapter)
        logging.debug("Looking up chapter at URL: {}".format(url))
        r = requests.get(url)
        if r.status_code != 200:
            logging.error("Could not look up {} {} at URL {}".format(
                book_name,
                book_chapter,
                url))
            raise Exception("Could not look up {} {} at URL {}".format(
                book_name,
                book_chapter,
                url))
        chapter_html = r.text
        soup = BeautifulSoup(chapter_html, 'html.parser')
        verses_list_soup = soup.get_text().split('\n')
        # Clean up verses list. This is being done because some
        # non-alphanumeric ASCII characters might have been picked up from the
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

        logging.debug("Successfully built list for {} chapter {}".format(
            book_name,
            book_chapter))

        return verses_list

    def verse_lookup(self, book_name, book_chapter, verse):
        """
        Looks up a verse from online.recoveryversion.bible, then returns it.
        """
        verses_list = self.get_online_chapter(book_name, str(book_chapter))
        return verses_list[int(verse) - 1]

    def get_book_number(self, book):
        # Adding one because lists are indexted starting with zero
        return self.BIBLE.keys().index(book) + 1

    def _remove_non_ascii(self, text):
        return ''.join(i for i in text if ord(i)<128)
