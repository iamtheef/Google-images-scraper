#!/usr/bin/env python

import os
import sys
import optparse

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


if __name__ == '__main__':
    scraper = Scraper()
    scraper.make_dir()