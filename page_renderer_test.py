import unittest
from unittest.mock import MagicMock

from page_renderer import PageRenderer
from pages import Pages


def return_true_if_param_is_junk(word: str):
    return word.lower() == "junk"


class PageRendererTest(unittest.TestCase):

    def test_markup_page_upper_case_goes_lower(self):
        self.assertEqual(PageRenderer.markup_page("Junk"), "junk.md")

    def test_markup_page_lower_case_stays_lower(self):
        self.assertEqual(PageRenderer.markup_page("junk"), "junk.md")

    def test_with_markup_link_includes_page(self):
        self.assertEqual(PageRenderer.with_markup_link("Stuff"), "[Stuff](stuff.md)")

    def test_sentence_without_a_word_matching_a_page_is_unchanged(self):
        toc = Pages(path_to_pages="")
        toc.word_matches_a_page = MagicMock(return_value=False)
        rend = PageRenderer(toc=toc)
        sentence = "A cow jumps over 3 moons, so it must be on Jupiter? I think so. "
        self.assertEqual(sentence, rend.transform(sentence))

    def test_sentence_with_page_match_includes_markup_link(self):
        toc = Pages(path_to_pages="")
        toc.word_matches_a_page = return_true_if_param_is_junk
        rend = PageRenderer(toc=toc)
        self.assertEqual("Stuff is [Junk](junk.md).", rend.transform("Stuff is Junk."))


if __name__ == '__main__':
    unittest.main()
