# pylint: disable=C0103
''' Program to sort a list using custom compare function'''

def my_list_compare(my_list1, my_list2):
    ''' Custom comparision function for our list '''
    if (len(my_list1) == len(my_list2)) and len(my_list1) > 1:
        if my_list1[1] == my_list2[1]:
            return 0
        elif my_list1[1] > my_list2[1]:
            return 1
        else:
            return -1
    else:
        return cmp(my_list1, my_list2)   #use standard compare function


my_list_of_list = [["john", 1, "a"], 	\
		   ["larry", 10, "b"],  \
	   	   ["xyz", 12, "c"], 	\
		   ["yuv", 5, "z"]]

print 'Original list is ', my_list_of_list
my_list_of_list.sort(my_list_compare)
print 'Sorted list is ', my_list_of_list
