#!/usr/bin/env python

import os
import optparse
from download import _download

class Scraper:
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option("-t", "--term", dest="term", help="A term to search for")
        self.parser.add_option("-v", "--volume", dest="volume", help="How many images you want to download")
        self.parser.add_option("-p", "--path", dest="path", help="Where you wanna save the images")

    def get_args(self):
        return self.parser.parse_args()[0]


    def make_dir(self):
        os.chdir('..')
        os.mkdir(self.get_args().path)
        print('[+] Creating directory')
        return os.path.join(os.getcwd() + '/' + self.get_args().path)


    def download_images(self, directory):
        print("[+] Downloading images")
        for _ in range(0, self.get_args().volume):
            _download(directory,  self.get_args().term)

if __name__ == '__main__':
    scraper = Scraper()
    # path = scraper.make_dir()
    # scraper.download_images(path)
    # # scraper.print_progress()