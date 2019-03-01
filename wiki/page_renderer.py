import re

from wiki.pages import Pages


class PageRenderer:
    """Rewrites text into the same text with a link around a word that matches the title of a wiki page."""

    def __init__(self, toc: Pages):
        self._pages = toc

    def transform(self, text: str) -> str:
        """:returns the given text with a link around any word that matches a page title"""
        results = ""
        for word in re.split('(\W)', text):
            formatted_word = word
            if self._pages.word_matches_a_page(word):
                formatted_word = PageRenderer.with_markup_link(word)
            results += formatted_word
        return results

    @staticmethod
    def with_markup_link(word: str) -> str:
        """:returns the word as a markup link to markup page"""
        return "[{word}]({page})".format(word=word, page=PageRenderer.markup_page(word))

    @staticmethod
    def markup_page(word: str) -> str:
        """:returns the file name where the wiki page will reside for a word"""
        return "{word}.md".format(word=word.lower())
