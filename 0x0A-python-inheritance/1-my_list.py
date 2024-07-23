#!/usr/bin/python3
""" 
avsimple module
"""
class MyList(list):
    pass
    def print_sorted(self):
        """ sort
        function
        """
        li = self[:]
        li.sort()
        print(li)
        
