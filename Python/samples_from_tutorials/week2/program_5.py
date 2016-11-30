# pylint: disable=C0103
'''

Program to reverse a given number

'''
original_number = input("Enter a number: ")
if isinstance(original_number, int) or isinstance(original_number, long):
    reverse_number = 0
    number = original_number
    while number > 0:
        reverse_number = (reverse_number*10) + (number%10)
        number /= 10

    print "Number = %d Reverse Number = %d" %(original_number, reverse_number) 

    # Method 2 converting the number into string and using range
    number_str = str(original_number)
    reverse_str = number_str[::-1]
    print "Number = %s and Reverse Number = %s" %(number_str, reverse_str)

else:
    print "Enter a valid integer value"
