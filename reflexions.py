# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:41:59 2016

@author: mika
"""
"""
To build the filename i need: the model names, a title and a category.

Based on files already scanned, i have a dictionary that provide models
names, titles and the categories for each entries.

I start from a filename.
This filename provides keywords i use to search a dictionary.
Based on this search,i have results for the models and the title.
I can guess the category based on the categories associated with each
valid dictionary entries in the results.

So basically:

for each keyword found in the dictionnary i build a set of results
This set of results have to be analyzed to clear false results
and decide what is the appropriate category (and therefore index)

for keyword in keywords_list:
    results = dictionary.check( keyword )
    if results:
        


"""