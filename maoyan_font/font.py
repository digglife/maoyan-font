# -*- coding: utf-8 -*-
import io
import requests
from fontTools.ttLib import TTFont

SAMPLE_FONT_URL = 'http://vfile.meituan.net/colorstone/2c8d9a8f5031f26f4e9fe924263e31ce2076.woff'
SAMPLE_FONT_MAPPING = {
    'uniE851': 0,
    'uniEBCF': 1,
    'uniF38E': 2,
    'uniE824': 3,
    'uniEFFE': 4,
    'uniE829': 5,
    'uniEDEE': 6,
    'uniF35D': 7,
    'uniF3C5': 8,
    'uniEE5A': 9
}

class MaoyanFontParser:
    def __init__(self):
        self._init_glyphs_mapping()

    def _init_glyphs_mapping(self):
        font = TTFont(io.BytesIO(requests.get(SAMPLE_FONT_URL).content))
        glyph_set = font.getGlyphSet()
        glyphs = glyph_set._glyphs.glyphs
        self.glyphs_mapping = {}
        for uni, number in SAMPLE_FONT_MAPPING.items():
            self.glyphs_mapping[glyphs[uni].data] = number

    def load(self, url):
        return MaoyanFont(url, self.glyphs_mapping)


class MaoyanFont:

    def __init__(self, url, mapping):
        self._url = url
        self._glyphs = None
        self.mapping = mapping

    @property
    def glyphs(self):
        if not self._glyphs:
            font = TTFont(io.BytesIO(requests.get(self._url).content))
            glyph_set = font.getGlyphSet()
            self._glyphs = glyph_set._glyphs.glyphs
        return self._glyphs

    def uni_to_number(self, uni):
        return self.mapping[self.glyphs[uni].data]

    def normalize(self, codes):
        number = ''
        for c in codes:
            uni = 'uni{:X}'.format(ord(c))
            if uni in self.glyphs:
                number += str(self.uni_to_number(uni))
            else:
                number += c
        return number
