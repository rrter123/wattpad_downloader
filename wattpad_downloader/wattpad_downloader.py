from .page_fetcher import WattpadPageFetcher
from .file_writer import FileTXTWriter
from .page_parser import SimpleTXTPageParser
from .logger import InfoLogger
from .page_dataclass import PageWithCount


class WattpadDownloader:
    def __init__(
        self,
        link: str,
        filename: str,
        fetcher=WattpadPageFetcher,
        parser=SimpleTXTPageParser,
        writer=FileTXTWriter,
    ):
        self.link = link
        self.filename = filename
        self.page_fetcher = fetcher(link)
        self.page_parser = parser
        self.file_writer = writer(filename)

    def download(self):
        pages = self.page_fetcher.give_pages_with_count()
        all_chapter_count = self.page_fetcher.give_chapter_count()
        self.logger = InfoLogger(all_chapter_count)
        self.logger.log_initial(self.link, self.filename)
        for page in pages:
            self.process_page(page)
        self.logger.log_final()

    def process_page(self, page: PageWithCount):
        self.logger.log_chapter(page)
        self.file_writer.write_chapter_info(page.chapter_number, page.chapter_name)
        text = self.page_parser.parse_page(page.page)
        self.file_writer.write(text)
