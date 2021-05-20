from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class Page:
    chapter_name: str
    page: BeautifulSoup


@dataclass
class PageWithCount(Page):
    chapter_number: int
    page_number: int
