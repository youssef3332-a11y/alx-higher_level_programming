#!/usr/bin/python3
""" 
avsimple module
"""
class MyList(list):
    def print_sorted(self):
        """ sort
        function
        """
        copy = self[:]
        copy.sort()
        print(copy)
