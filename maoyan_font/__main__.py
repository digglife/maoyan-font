#!/usr/bin/env python
# coding: utf-8

"""Demo CLI program for maoyan-font
"""
import sys
import re
import argparse
import requests
from bs4 import BeautifulSoup
from .font import MaoyanFontParser

chrome = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36'
          ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')

def get_box(movie_url):
    res = requests.get(movie_url, headers={'User-Agent': chrome}).text
    html = BeautifulSoup(res, 'html.parser')

    font_url = 'http:' + re.search(r'url\(\'(.*\.woff)\'\)', res).group(1)

    parser = MaoyanFontParser()
    font = parser.load(font_url)

    name = html.select_one('h3.name').text
    movie_status = html.select_one('div.movie-stats-container')
    box_unit = movie_status.select_one('div.box > span.unit')
    if box_unit:
        raw_box = movie_status.select_one('div.box > span.stonefont')
        box_num = font.normalize(raw_box.text)
        box = box_num + box_unit.text
    else:
        box = None

    return {'name': name, 'box': box}

def main():
    parser = argparse.ArgumentParser(description='get box office info via url')
    parser.add_argument('url', help='movie url to parse')

    if not sys.argv:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    box = get_box(args.url)
    print(box)

if __name__ == "__main__":
    main()
