# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:32:13 2016

@author: mika
"""

class Entry:
    
    def __init__(self, entry, label, category):
        from utility.tools import flip_words
        self.entry      = flip_words(entry)
        self.label      = label
        self.categories = set(category)
        
    def add_category(self, category):
        self.categories.add(category)
        
    def __repr__(self):
        return "{} ({})".format(self.entry, self.label)

class Dictionary:
    """
    Le Dico permet de stocker un ensemble d'entrées relative 
    à un type d'information
    """
    entries = list()

    @staticmethod        
    def add(self, entry):
        """
        ajoute une entrée dans le dictionnaire
        """
        Dictionary.entries.add(entry)
    
    @staticmethod
    def categories(entry):
        """
        renvoie la liste des categories associée à une entrée
        ou une liste vide sinon
        """
        for entry in Dictionary.entries:
            if entry.words == words:
                return entry.categories
            
        return None

    @staticmethod
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
            for entry in self.entries.keys():
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
        
if __name__ == "__main__":
    
    