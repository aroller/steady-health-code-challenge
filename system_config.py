class SystemConfig:

    @staticmethod
    def pages_path() -> str:
        """:returns the path to the directory where the pages are located"""
        return "pages"

    @staticmethod
    def docs_path() -> str:
        """:returns the path to the directory where the docs are generated"""
        return "docs"
