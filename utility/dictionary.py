# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 07:48:21 2016

@author: mika
"""

class Dictionary:
    """
        Le Dico permet de stocker un ensemble d'entrées relative 
        à un type d'information
    """
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.entries = list()
        
    def add(self, words, category):
        """
            ajoute une entrée dans le dictionnaire
        """
        from utility.tools import flip_words
        entry_exists = False
        
        words = flip_words(words)
        
        for entry in self.entries:
            if entry['words'] == words:
                entry_exists = True
                if category not in entry['categories']:
                    entry['categories'].append(category)
        if not entry_exists:
            self.entries.append({'words': words, 'categories': [category]})
            self.count += 1
            self.entries = sorted(self.entries, key=lambda e: e['words'], reverse=True)
            
    def categories(self, words):
        """
        renvoie la liste des categories associée à une entrée
        ou une liste vide sinon
        """
        for entry in self.entries:
            if entry['words'] == words:
                return entry['categories']
                
        return []

    def check(self, words):
        """
            vérifie si le mot est dans le dico
            retourne une valeur basée sur la pertinence de la recherche
        """
        from utility.tools import flip_words
        from utility.const import BASE_SCORE
        results = list()
        
        for i in range(0, len(words)):
            score = 0
            for entry in self.entries:
                current_score = 0
                current_word = flip_words(words[i])
                if current_word.lower() in entry['words'].lower() or \
                   current_word.lower() in entry['words'].lower().replace(" ", ""):
                    if current_word.lower() in entry['words'].lower():
                        current_score = len(current_word)/len(entry['words'])
                    if current_word.lower() in entry['words'].lower().replace(" ", ""):
                        current_score = len(current_word)/len(entry['words'].replace(" ", ""))

                    for j in range(1,len(words)-i):
                        if i < len(words)-j:
                            new_word = " ".join([current_word, words[i+1]])
                            if new_word.lower() in entry['words'].lower():
                                current_score = len(new_word)/len(entry['words'])
                                current_word = new_word
                                i += 1
                            else:
                                break
                        else:
                            break
                    if current_score > score:
                        if {"word": entry['words'], "score": score} not in results:
                            current_guess = {"word": entry['words'], "score": current_score}
                            score = current_score
            if score > BASE_SCORE:
                results.append(current_guess)
        
        return sorted(results, key=lambda r: r['score'], reverse=True )
        
    def __repr__(self):
        return self.name
