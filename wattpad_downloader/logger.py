import time
from .page_dataclass import PageWithCount


class InfoLogger:
    def __init__(self, all_chapters_count):
        self.all_chapters_count = all_chapters_count
        self.start = time.time()

    def log_initial(self, link: str, filename: str):
        print("Link to Story:", link)
        print("Filename:", filename)
        print(f"Chapter amount: {self.all_chapters_count}")

    def log_chapter(self, page: PageWithCount):
        print(
            f"Processing chapter {page.chapter_number + 1}/{self.all_chapters_count} "
            f"[{round(page.chapter_number/self.all_chapters_count*100.0, 2)}%]: "
            f"{page.chapter_name}, page: {page.page_number}           ",
            end="\r",
        )

    def log_final(self):
        print(f"Done in {time.time() - self.start} seconds." + " " * 30)
