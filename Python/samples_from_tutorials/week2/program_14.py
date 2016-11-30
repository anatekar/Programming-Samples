# pylint: disable=C0103
'''

Program to determine if an year is a leap year

'''

def is_leap(year):
    '''
        Determine if a year is leap year or not
    '''
    if (year % 4 == 0) and (year % 200 != 0):
        return True
    else:
        return False


year_str = raw_input("Enter a year: ")
if year_str.isdigit():
    year_from_user = eval(year_str)
    if is_leap(year_from_user):
        print 'Year %d is a leap year' % year_from_user
    else:
        print 'Year %d is not a leap year' % year_from_user
else:
    print 'Year not a valid number'

