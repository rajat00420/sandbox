__author__ = 'jc441938'
y, x =5.5,"jay"
try:
    result= x*y
    print(result)
except ValueError:
    print("value")
except TypeError:
    print("type")
except:
        print("other")