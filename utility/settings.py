# -*- coding: utf-8 -*-
"""
@author: mika
"""

from os      import getenv
from os.path import join
from os.path import curdir
from os.path import isfile 
from json    import load
from json    import dump

class Settings:
    
    BASE_SCORE = 0.7

    INPUT_DIR = join(getenv('HOME'), '.data/.other/_input')

    MEDIA_DIR_LIST = [ 
        join(getenv('HOME'), '.data/.other/s'),
        join(getenv('HOME'), '.data/.other/l'),
        join(getenv('HOME'), '.data/.other/m'),
        join(getenv('HOME'), '.data/.other/c') ]

    MEDIA_EXT = [ "mp4", "wmv", "mpeg", "mpg", "avi", "flv" ]

    TRASH_LIST = [ "XXX", "mp4", "480p", "720p", "1080p" ]

    STUDIO_LIST =[ "Brazzers", "Reality Kings", "Naughty America" ]

    SHORT_NAMES = [
        {'short': "bex", 'long': "Brazzers Extra"},
        {'short': "tlib", 'long': "Teens Like It Big"},
        {'short': "plib", 'long': "Pornstars Like It Big"},
        {'short': "mic", 'long': "Moms In Control"} ]

    def __init__(self):
        settings_file = join( curdir, "settings.json" )
        if isfile( settings_file ):
            self.load_settings_from_file( settings_file )
        else:
            for attr in Settings.__dict__:
                if attr.startswith('__') or attr[0].islower():
                    continue
                setattr( self, attr, getattr(self, attr) ) 
                self.save_settings_to_file( settings_file )

    def save_settings_to_file(self, settings_file):
        try:
            with open( settings_file, "w" ) as f:
                dump( self.__dict__, f, indent=True )
        except:
            return False

    def load_settings_from_file(self, settings_file):
        try:
            with open( settings_file, "r" ) as f:
                settings = load(f)
            for attr, value in settings.items():
                setattr( self, attr, value )
        except:
            pass
