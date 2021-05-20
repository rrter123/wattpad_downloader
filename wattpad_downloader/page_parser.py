class SimpleTXTPageParser:
    @classmethod
    def parse_page(cls, page_content):
        text = ""
        for paragraph in cls.get_all_paragraphs(page_content):
            text += paragraph.get_text() + "\n"
        return text

    @classmethod
    def get_all_paragraphs(self, page_content):
        return page_content.find_all("p", class_=None)

    @classmethod
    def check_if_page_empty(cls, page_content):
        return len(cls.get_all_paragraphs(page_content)) > 0
