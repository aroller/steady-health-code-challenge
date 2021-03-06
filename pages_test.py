import unittest

from system_config import SystemConfig
from pages import Pages


class PagesTest(unittest.TestCase):

    def __init__(self, method_name):
        super().__init__(method_name)
        self._toc = Pages(SystemConfig.pages_path())

    def test_page_filename(self):
        self.assertEqual(Pages.page_filename("Somewhere"), "Somewhere.txt")

    def test_path_to_page(self):
        path = self._toc.page_path("Junk")
        self.assertEqual(path, "pages/Junk.txt")

    def test_page_wiki_exists(self):
        self.assertTrue(self._toc.word_matches_a_page("Wiki"))

    def test_lower_case_wiki_does_exist(self):
        self.assertTrue(self._toc.word_matches_a_page("wiki"))

    def test_nothing_does_not_exist(self):
        self.assertFalse(self._toc.word_matches_a_page("Nothing"))

    def test_pages_are_in_all_pages(self):
        pages = self._toc.all_page_filenames()
        self.assertIn("Wiki.txt", pages)
        self.assertIn("Nelson.txt", pages)
        self.assertIn("Cunningham.txt", pages)


if __name__ == '__main__':
    unittest.main()
