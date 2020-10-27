from scrapy.cmdline import execute

import sys
import os



##
def run_spider():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.abspath(__file__)))
    # execute(["scrapy", "crawl", "hnust"])
    execute("scrapy crawl hnust".split())

if __name__ == "__main__":
    run_spider()
