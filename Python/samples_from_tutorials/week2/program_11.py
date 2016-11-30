# pylint: disable=C0103
'''
    Program to determine if a number is prime or not
    and if its an amstrong number or not

'''

def is_prime(num):
    ''' Determines if a number is prime or not'''
    for n in range(2, num-1):
        if num%n == 0:
            return False
    return True

def get_cube(n):
    ''' Returns cube of a number i.e. n*n*n'''
    return n*n*n

def is_armstrong(num):
    ''' determines if a number is an armstrong number or not'''
    armstrong_sum = 0
    number_str = str(num)
    for value in number_str:
        armstrong_sum += get_cube(int(value))
    if armstrong_sum == num:
        return True
    else:
        return False


def print_ascii(num):
    ''' Print's ascii value for each digit in the number'''
    number_str = str(num)
    for value in number_str:
        print ord(value),


number = input("Enter a number: ")
print 'Number %d is %s' %(number, 'Prime' if is_prime(number) == True \
						else 'not prime')
print 'Number %s is %s' %(number, 'Amstrong' if is_armstrong(number) == True \
						 else 'Not Armstrong')
print_ascii(number)
