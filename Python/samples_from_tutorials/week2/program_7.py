# pylint: disable=C0103
'''

    Program to create Fibonacci series of n numbers

'''



def fibonacci(n):
    '''
    Function to print fibonacci series for n numbers
    '''

    next_fibonacci = 1
    previous_fibonacci = 0
    while n > 0:
        print previous_fibonacci,
        temp = next_fibonacci
        next_fibonacci += previous_fibonacci
        previous_fibonacci = temp
        n -= 1
    

number = input("Enter a number: ")
fibonacci(number)   
