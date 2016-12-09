'''
    Sample program to reverse list within list
'''

import copy

def reverse_list_within_list(example_list):
    ''' Reverses list within list using list comprehension function '''
    [list_item.reverse() for list_item in example_list]
    return 0

def reverse_list_within_list_using_map(example_list):
    ''' Reverses list within list using map '''
    map(list.reverse, example_list)


def main():
    ''' Main function '''
    my_list = [["Abc", 35],["DEF", 36],["XYZ", 40]]
    my_list2 = copy.deepcopy(my_list)
    print 'Original List ', my_list
    reverse_list_within_list(my_list)
    print 'Reversed List', my_list
    reverse_list_within_list_using_map(my_list2)
    print 'Reversed using map', my_list2

main()
