# Using Bulk Bing image downloader
#  bbid.py --limit 100 -o <output_directory> "car"

from icrawler.builtin import BingImageCrawler

# "automobile",
# airplane
categories = [
    "automobile",
    "airplane",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def smart_download(category, count):
    # This crawler is much smarter about 'indexing'
    crawler = BingImageCrawler(storage={"root_dir": f"data/scrapped/{category}"})
    crawler.crawl(keyword=category, max_num=count)


for category in categories:
    print(f"Downloading images for: {category}")
    smart_download(category, 100)
