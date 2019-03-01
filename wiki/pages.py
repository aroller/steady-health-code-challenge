import os
from typing import List


class Pages:
    """Knows about all of the pages participating in the wiki.
    """

    def __init__(self, path_to_pages: str):
        self._path_to_pages = path_to_pages
        """The path to the folder containing the pages."""

    def word_matches_a_page(self, word: str) -> bool:
        """Checks the given word to see if a page title matches.
        :param word found in the text of a page that may match the title of a page
        @:returns true if a page is found with a title that matches the word (case insensitive)
        """
        return os.path.exists(self.page_path(word))

    def page_path(self, word) -> str:
        """Builds the entire path to the page that would match the given word.
            :param word found in the text of a page that may match the title of a page...must match case and spaces exactly
            :returns path to the potential page
        """
        return "{path}/{page}".format(path=self._path_to_pages, page=Pages.page_filename(word))

    @staticmethod
    def page_filename(word: str) -> str:
        """:returns the filename for a source page for the word"""
        return "{page}.txt".format(page=word)

    def all_page_filenames(self) -> List[str]:
        """:returns all known source pages found in the path_to_pages."""
        return os.listdir(self._path_to_pages)
