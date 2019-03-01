import os

from wiki.page_renderer import PageRenderer
from wiki.system_config import SystemConfig
from wiki.table_of_contents import TableOfContents


def generate_wiki():
    """Reads each page in the pages directory and writes a markup page in the docs directory that will contain
    text that will link to other pages if they match the words."""
    toc = TableOfContents(SystemConfig.pages_path())
    rend = PageRenderer(toc=toc)

    for page_filename in toc.all_page_filenames():
        contents = page_contents(page_filename)
        write_contents(contents, page_filename, rend)


def write_contents(contents, page_filename, rend):
    formatted_contents = rend.transform(contents)
    title = strip_suffix(page_filename)
    doc_filename = rend.markup_page(title)
    doc_filepath = "../docs/{filename}".format(filename=doc_filename)
    docs_file = open(doc_filepath, "w+")
    docs_file.write(formatted_contents)
    docs_file.close()


def page_contents(page_filename):
    page_filepath = "{path}/{filename}".format(path=SystemConfig.pages_path(), filename=page_filename)
    page_file = open(page_filepath, "r")
    contents = page_file.read()
    page_file.close()
    return contents


def strip_suffix(name: str) -> str:
    """:returns the name from a filename stripping off the suffix."""
    return name.split(".")[0]


if __name__ == '__main__':
    generate_wiki()
