# pylint: disable=C0103
'''
    Program to find factorial of a user defined number
'''

def fact(n):
    ''' Return factorial of number n i.e. n! '''
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

number = input("Enter a number: ")
print '%d! = %d' %(number, fact(number))
