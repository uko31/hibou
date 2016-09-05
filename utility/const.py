# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:00:46 2016

@author: mika
"""

from os      import getenv
from os.path import join

BASE_SCORE = 0.7

INPUT_DIR = join(getenv('HOME'), '.data/.other/_input')

MEDIA_DIR_LIST = [ join(getenv('HOME'), '.data/.other/s'),
                    join(getenv('HOME'), '.data/.other/l'),
                    join(getenv('HOME'), '.data/.other/m'),
                    join(getenv('HOME'), '.data/.other/c') ]

MEDIA_EXT = [ "mp4", "wmv", "mpeg", "mpg", "avi", "flv" ]

TRASH_LIST = [
  "XXX", "mp4", "480p", "720p", "1080p"
]

STUDIO_LIST =[ "Brazzers", "Reality Kings", "Naughty America" ]

SHORT_NAMES = [
    {'short': "bex", 'long': "Brazzers Extra"},
    {'short': "tlib", 'long': "Teens Like It Big"},
    {'short': "plib", 'long': "Pornstars Like It Big"},
    {'short': "mic", 'long': "Moms In Control"} ]