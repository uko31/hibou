# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 07:47:29 2016

@author: mika
"""

import re

class Media:
    """
    Gestion des fichiers media
    """
    def __init__(self, filename):
        self.filename = filename
        
    def __repr__(self):
        return self.filename
        
    def get_keywords_list(self):
        """
        1) je supprime 'BASE_DIR' de la chaine de recherche
        2) je supprime l'extension
        3) je crée un tableau de mots sur la base de la chaine de recherche
        4) je supprime les nombres
        5) je supprime les mots connus (TRASH_LIST)
        """

        from utility.const import INPUT_DIR
        from utility.const import TRASH_LIST
        keywords_list = list()
        tmp_list = list()
        
        name = self.filename.replace(INPUT_DIR, "")
        name = name.rsplit(".", 1)[0]
        
        tmp_list = re.findall(
          r'(?P<word>[\w]{2,})\b', 
          name.replace("_", " ")
        )
        
        for word in tmp_list:
          try:
            int(word)
          except:
            keywords_list.append(word)
    
        tmp_list = keywords_list
        keywords_list = list()
        for word in tmp_list:
          if word not in TRASH_LIST and word.lower() not in keywords_list:
            keywords_list.append(word.lower())
            
        return keywords_list