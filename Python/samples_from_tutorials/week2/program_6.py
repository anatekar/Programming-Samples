# pylint: disable=C0103
'''
Program to find unique,duplicate and distinct elements of a list
'''

def get_unique(list_of_numbers):
    ''' gets unique elements of a list'''
    return [unique_list for unique_list in list_of_numbers \
				if list_of_numbers.count(unique_list) == 1]

def get_duplicates(list_of_numbers):
    ''' gets duplicate elements of a list'''
    duplicate_set = set([duplicates for duplicates in list_of_numbers \
					if list_of_numbers.count(duplicates) > 1])
    return list(duplicate_set)

def get_distinct(list_of_numbers):
    '''gets distinct elements of a list'''
    return get_unique(list_of_numbers) + get_duplicates(list_of_numbers)

statement = raw_input('Enter list of numbers seperated by space: ')
list_of_num = statement.split(' ')
print get_unique(list_of_num)
print get_duplicates(list_of_num)
print get_distinct(list_of_num)

