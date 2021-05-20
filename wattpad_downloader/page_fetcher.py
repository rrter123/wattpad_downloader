from functools import cached_property
from .base_connection_mixin import BaseConnectionMixin
from .iterators import WattpadPageIterator, WattpadPageWithCountIterator


class WattpadPageFetcher(BaseConnectionMixin):
    def __init__(self, link):
        self.base_link = link

    @cached_property
    def parts(self):
        base_page_soup = self.get(self.base_link)
        parts_div_soup = self.get_parts_div(base_page_soup)
        parts = []
        for link in parts_div_soup.find_all("a"):
            chapter_name = link.get_text()
            chapter_link = self.create_full_link(link.get("href"))
            chapter_tuple = (chapter_name, chapter_link)
            parts.append(chapter_tuple)
        return parts

    def give_pages(self):
        return WattpadPageIterator(self.parts)

    def give_pages_with_count(self):
        return WattpadPageWithCountIterator(self.parts)

    def give_chapter_count(self):
        return len(self.parts)

    def create_full_link(self, partial_link: str):
        return "https://www.wattpad.com" + partial_link

    def get_parts_div(self, soup):
        parts_class = "story-parts"
        found = soup.find_all("div", class_=parts_class)
        return found[0]
