class BaseFileWriter:
    def __init__(self, filename):
        if self.file_extension in filename:
            self.filename = filename
        else:
            self.filename = filename + self.file_extension
        self.clean_file()
        self.latest_chapter = -1

    def clean_file(self):
        open(self.filename, "w").close()


class FileTXTWriter(BaseFileWriter):
    """
    Class that handles creating and writing to the final output txt file
    """
    file_extension = ".txt"

    def write_chapter_info(self, chapter_number, chapter_name):
        if self.latest_chapter != chapter_number:
            self.new_chapter(chapter_name)
            self.latest_chapter = chapter_number

    def new_chapter(self, chapter_name):
        with open(self.filename, "a+", encoding="UTF-8") as f:
            f.write("-" * 10 + "\n")
            f.write(chapter_name + "\n")
            f.write("-" * 10 + "\n")

    def write(self, chapter_content):
        with open(self.filename, "a+", encoding="UTF-8") as f:
            f.write(chapter_content)


class FileEBUPWriter:
    pass  # TODO Create this here :D
