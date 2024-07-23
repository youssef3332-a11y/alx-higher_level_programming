from models import teest
def func(arg, *args, **kwargs):
    print("arg:{}".format(arg))
    print("args:{}".format(args))
    print("kwargs:{}".format(kwargs))
    
    
func(1, 2, 3, 4, midle=5, six=6, seven=7)