# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 07:47:36 2016

@author: mika
"""

class Performer:
    """
    To be continued
    """
    def __init__(self, lastname, firstname="", categories=None):
        self.lastname = "Doe" if lastname == ''else lastname
        self.firstname  = firstname
        self.categories = categories if categories else set()
    
    def __repr__(self):
        return self.firstname+self.lastname
    
    def __str__(self):
        performer = ""
        if self.firstname: performer += self.firstname
        performer += self.lastname
        if self.categories:
            for c in self.categories:
                performer+=str(c)

        return performer        
        
    
if __name__ == "__main__":
    try:
        p = Performer("")
        assert p.__repr__() == "Doe", \
            "Error, Performer __init__ with lastname = '': '{}'".format(p)
        
        p = Performer("Doe")
        assert p.__repr__() == "Doe", \
            "Performer __init__ with no firstname nor categories"
    
        p = Performer("Doe", firstname="John")
        assert p.__repr__() == "JohnDoe", \
            "Performer __init__ with no categories"
    
        p = Performer("Doe", categories={'c', 'l', 's'})
        assert p.__repr__() == "Doe", \
            "Performer __init__ with no firstname"
    
        p = Performer("Doe", firstname="John", categories=None)
        assert p.__repr__() == "JohnDoe", \
            "Performer __init__ with categories explicit to None"
    
        p = Performer("Doe", firstname="John", categories={1,2,3})
        assert p.__repr__() == "JohnDoe", \
            "Performer __init__ with all arguments"
    except AssertionError as e:
        print(str(e))
    else:
        print("All test cases ok")
