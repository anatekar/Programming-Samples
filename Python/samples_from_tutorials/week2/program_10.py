# pylint: disable=C0103
'''
    Program to find greatest of 3 numbers
'''

def greatest(x, y, z):
    ''' Function to return greatest of 3 numbers '''
    greater = x
    if greater < y:
        greater = y
    if greater < z:
        greater = z
    return greater

def greatest_using_iterable(*args):
    '''Function to return greatest using iterable data structure '''
    print args
    return max(args)

number1 = raw_input("Enter number 1: ")
number2 = raw_input("Enter number 2: ")
number3 = raw_input("Enter number 3: ")
print 'Greater of (%r %r %r) is %r' %(number1, number2, number3, \
					greatest(int(number1), int(number2), int(number3)))
print 'Greater of (%r %r %r) is %r' %(number1, number2, number3, \
					greatest_using_iterable(int(number1), int(number2), int(number3)))
