'''
	Program to swap two numbers entered by the user
'''
# pylint: disable=C0103
Number1 = input("Enter 1st number: ")
Number2 = input("Enter 2nd number: ")
print "Original numbers are Number1 = %d and number2 = %d" % (Number1, Number2)
Number1 += Number2
Number2 = Number1 - Number2
Number1 = Number1 - Number2
print "After swapping Number1= %d and Number2 = %d" % (Number1, Number2)
