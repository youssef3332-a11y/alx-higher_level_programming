class rectangle:
    def __init__(self, width, height):
       self.width = width
       self.height = height 
    def func(self, *args):
        for i in range(len(args)):

            print(len(args))
dic={"youssef":21, "yassine":14}
for key, value in dic.items():
    print(key)
    print("...")
    print(value)