class rectangle:
    def __init__(self, width, height):
       self.width = width
       self.height = height 
    def func(self, *args):
        for i in range(len(args)):
            
        print(len(args))
r=rectangle(3,5)
r.func(4,34,5,6)