import unittest

from wiki.system_config import SystemConfig
from wiki.table_of_contents import TableOfContents


class TableOfContentsTest(unittest.TestCase):

    def __init__(self, method_name):
        super().__init__(method_name)
        self._toc = TableOfContents(SystemConfig.pages_path())

    def test_path_to_page(self):
        path = self._toc._page_path("Junk")
        self.assertEqual(path,"../pages/Junk.txt")

    def test_page_wiki_exists(self):
        self.assertTrue(self._toc.word_matches_a_page("Wiki"))

    def test_lower_case_wiki_does_exist(self):
        self.assertTrue(self._toc.word_matches_a_page("wiki"))

    def test_nothing_does_not_exist(self):
        self.assertFalse(self._toc.word_matches_a_page("Nothing"))

