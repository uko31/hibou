# -*- coding: utf-8 -*-
"""

"""

import pickle
import os.path
import sys

from utility.settings import Settings
from utility.const import INPUT_DIR
from utility.const import MEDIA_DIR_LIST
from utility.tools import init_dictionaries
from utility.tools import get_media_list
from utility.tools import parse_media_keywords
from utility.tools import analyse_results
from utility.color import Color as c

if __name__ == "__main__":
    """
    ce programme permet de deviner les noms de fichiers et de les renommer
    en accord avec ce qui a été trouvé dans les dictionnaires.
    """    
    
    settings = Settings()
    print(settings.STUDIO_LIST)

    # a faire plus tard: gérer les options de lancement pour modifier
    # le comportement par défaut.
    
    # on contruit les dictionnaires et la liste des fichiers à travailler:
    #dictionaries = init_dictionaries(MEDIA_DIR_LIST)
    if os.path.isfile("dictionaries.dump"):
        with open("dictionaries.dump", "rb") as f:
            dictionaries = pickle.load(f)        
    else:
        dictionaries = init_dictionaries(MEDIA_DIR_LIST)
        with open("dictionaries.dump", "wb") as f:
            pickle.dump(dictionaries, f)
            
    media_list   = get_media_list(INPUT_DIR)
    for media in media_list:
        print(c.green + "{}:".format(media.filename) + c.end)
        for dictionary in dictionaries:
            results = parse_media_keywords(media, dictionary)
            analyse_results(results, dictionary.name)
            
#            for result in sorted(results, key=lambda r: r['score'], reverse=True):
#                print(" > > found {} '{}' [{:.0%}]".format(dictionary.name, result['word'], result['score']))
                
#                """
#                key = input("agree [Y/n/q]: ")
#                if key == 'q':
#                    sys.exit()
#                if key == 'n':
#                    entry = input("Add new entry [N]: ")
#                    if entry:
#                        print("Add '' to dictionary {}".format(entry, dictionary.name))
#                    else:
#                        print("Ignore guess {}".format(result['word']))
#                    
#                else:
#                    print("Go for {} '{}'".format(dictionary.name, result['word']))
#                """

    
