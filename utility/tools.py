# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:58:29 2016

@author: mika
"""

from os      import walk
from os.path import join, isdir, isfile

from utility.const      import MEDIA_EXT
from utility.const      import STUDIO_LIST
from utility.dictionary import Dictionary
from utility.media      import Media

def flip_words(words):
    """
    utility to convert words like "IAmTheLaw" to "I Am The Law"
    """
    new_words = ""
    for i in range(0, len(words)):
        if words[i].isupper() and i > 0 and words[i-1].islower():
            new_words += " "
        new_words += words[i]
    return new_words

def init_dictionaries(media_dir_list):
    models = Dictionary("Models")
    titles = Dictionary("Titles")

    for directory in media_dir_list:
        for root, dirs, files in walk(directory):
            for filename in files:
                filename, filetype = filename.rsplit(".", 1)
                if filetype in MEDIA_EXT:
                    cast  = filename.split()[:-2]
                    title = filename.split()[-2]
                    cat   = filename.split()[-1][0]
          
                    for model in cast:
                        if model == "Friend": print(filename)
                        models.add(model, cat)
                    titles.add(title, cat)
            
    return [models, titles]
    
def get_media_list(filename):
    media_list = list()
  
    if isdir(filename):
        if not filename .endswith('/'):
            filename += '/'
        for root, dirs, files in walk(filename):
            for f in files:
                ext = f.rsplit(".", 1)[1]
                if ext in MEDIA_EXT:
                    name = join(root, f).replace(filename, "")
                    media = Media(name)
                    media_list.append(media)

    elif isfile(filename):
        ext = filename.rsplit(".", 1)[1]
        if ext in MEDIA_EXT:
            media = Media(filename)
            media_list.append(media)
    
    return media_list
    
def parse_media_keywords(media, dictionary):
    """
    
    """
    results = dict()
    keywords_list = media.get_keywords_list()
    results = dictionary.check(keywords_list)

    return results
    
def analyse_results(results, dictionary):
    """
    analyse les resultats et rationalise les informations trouvees
    """
    tmp_results = list()
    
    if dictionary == "Titles":
        for result in results:
            if result['score'] == 1:
                tmp_results.append(result)
                
        if len(tmp_results) == 0:
            print("Not able to guess the title")
            
        if len(tmp_results) == 1:
            print("Guessed title is: {}".format(tmp_results[0]['word']))
            
        if len(tmp_results) > 1:
            sorted_titles = list()
            print("more than one title found")
            for result in tmp_results:
                if result['word'] not in STUDIO_LIST:
                    sorted_titles.append(result['word'])
            if len(sorted_titles) == 1:
                print("Guessed title is: {}".format(sorted_titles[0]))
            else:
                print("Not able to guess the title")
            
        
    