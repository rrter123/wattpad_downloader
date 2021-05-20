from .base_connection_mixin import BaseConnectionMixin
from .page_parser import SimpleTXTPageParser
from .page_dataclass import Page, PageWithCount
from bs4 import BeautifulSoup

# Interesting info: ../page/0/ MIGHT give you an entire chapter
# That might be faster, but it would require further testing


class WattpadPageIterator(BaseConnectionMixin):
    """
    Class that iterates over an entire story page by page.
    """
    def __init__(self, chapter_list):
        self.chapter_list = chapter_list
        self.chapter_num = 0
        self.page_num = 1

    def __iter__(self):
        return self

    def create_page_link(self, chapter_link: str) -> str:
        return f"{chapter_link}/page/{self.page_num}"

    def __next__(self) -> Page:
        try:
            chapter_name, chapter_link = self.chapter_list[self.chapter_num]
        except IndexError:
            raise StopIteration
        page_link = self.create_page_link(chapter_link)
        page = self.get(page_link)
        if self.page_not_empty(page):
            self.page_num += 1
            return Page(chapter_name, page)
        self.chapter_num += 1
        self.page_num = 1
        return self.__next__()

    def page_not_empty(self, page: BeautifulSoup) -> bool:
        return SimpleTXTPageParser.check_if_page_empty(page)


class WattpadPageWithCountIterator(WattpadPageIterator):
    """
    An extension of the WattpadPageIterator class that returns more information
    """
    def __next__(self) -> PageWithCount:
        try:
            chapter_name, chapter_link = self.chapter_list[self.chapter_num]
        except IndexError:
            raise StopIteration
        page_link = self.create_page_link(chapter_link)
        page = self.get(page_link)
        if self.page_not_empty(page):
            self.page_num += 1
            return PageWithCount(chapter_name, page, self.chapter_num, self.page_num - 1)
        self.chapter_num += 1
        self.page_num = 1
        return self.__next__()
