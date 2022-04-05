try:
    x = int (input ("enter any number :"))
    y = int (input ("enter another number :"))
    div = x/y
    print (div)
except ValueError:
    print("\n!!! your value type is incorrect !!! ")
except ZeroDivisionError:
    print("\n!!! can't divide by 0 !!!")
