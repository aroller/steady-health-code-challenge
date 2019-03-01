from wiki.page_renderer import PageRenderer
from wiki.system_config import SystemConfig
from wiki.table_of_contents import TableOfContents


def generate_wiki():
    """Reads each page in the pages directory and writes a markup page in the docs directory that will contain
    text that will link to other pages if they match the words. Also creates a table of contents ."""
    toc = TableOfContents(SystemConfig.pages_path())

    index_file = open("{path}/index.md".format(path=SystemConfig.docs_path()), "w+")
    index_file.write("# Table of Contents\n")

    for page_filename in toc.all_page_filenames():
        contents = read_contents(page_filename)
        write_contents(contents, page_filename, toc)
        write_to_index(page_filename, index_file)

    index_file.close()


def write_contents(contents, page_filename, toc):
    """Formats the contents adding links to existing pages and writes to the corresponding markup file."""
    rend = PageRenderer(toc=toc)
    formatted_contents = rend.transform(contents)
    title = strip_suffix(page_filename)
    doc_filename = PageRenderer.markup_page(title)
    doc_filepath = "{path}/{filename}".format(path=SystemConfig.docs_path(), filename=doc_filename)
    docs_file = open(doc_filepath, "w+")
    docs_file.write(formatted_contents)
    docs_file.close()


def read_contents(page_filename) -> str:
    """:returns the contents from the source file"""
    page_filepath = "{path}/{filename}".format(path=SystemConfig.pages_path(), filename=page_filename)
    page_file = open(page_filepath, "r")
    contents = page_file.read()
    page_file.close()
    return contents


def write_to_index(page_filename, index_file):
    """writes the title of the filename to the index file providing a link to the page"""
    title = strip_suffix(page_filename)
    title_with_link = PageRenderer.with_markup_link(title)
    line = "* {}\n".format(title_with_link)
    index_file.write(line)


def strip_suffix(name: str) -> str:
    """:returns the name from a filename stripping off the suffix."""
    return name.split(".")[0]


if __name__ == '__main__':
    generate_wiki()
