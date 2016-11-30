# pylint: disable=C0103
'''
    Program to reverse/inverse a dictionary
'''

def inverse_key_values(original_dict):
    ''' Function to inverse key:value pairs of a dictionary'''
    new_dict = {}
    keys = original_dict.keys()
    values = original_dict.values()
    num_items = 0
    for value in values:
        new_dict[value] = keys[num_items]
        num_items += 1
    return new_dict


d = {1:'a', 2:'b', 3:'b'}
print 'Original dictionary is : ', d
print 'Inverse dictionary is :', inverse_key_values(d)
