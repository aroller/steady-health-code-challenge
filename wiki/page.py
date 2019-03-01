class Page:
    """Represents the data from a single wiki page"""

    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

    @property
    def title(self) -> str:
        return self._title

    @property
    def contents(self) -> str:
        return self._contents
