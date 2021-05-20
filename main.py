from wattpad_downloader import WattpadDownloader
import sys


# ask for link
link = sys.argv[1]
filename = sys.argv[2] if len(sys.argv) > 2 else "Downloaded Wattpad Story"
WattpadDownloader(link, filename).download()
