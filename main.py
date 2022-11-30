''' example module with a few math functions '''
def square(n):
    ''' returns the square of the parameter '''
    return n*n

def cube(n):
    return n*n*n

def weather(fahr):
    if fahr<50:
      print("it's cold outside")
    elif fahr<75:
      print("it's nice outside")
    else:
      print("it's hot outside")