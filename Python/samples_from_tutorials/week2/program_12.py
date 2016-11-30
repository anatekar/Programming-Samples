# pylint: disable=C0103
'''

    Program to count the number of words in a statement and to count the number
    of vowels in the complete statement
'''

def count_words(statement):
    ''' Returns the number of words in a statement'''
    list_of_words = statement.split(' ')
    #This is required if original statement has two or more spaces between words
    words = [word for word in list_of_words if len(word.strip()) > 0]
    #print words
    #print list_of_words
    return len(words)

def count_vowels(statement):
    '''Returns the number of vowels in the statement'''
    vowels = "aeiouAEIOU"
    number_of_vowels = len([character for character in statement \
					if character in vowels])
    return number_of_vowels

stmt = raw_input("Enter your statement: ")
print 'Number of words = %d' % count_words(stmt)
print 'Number of vowels = %d' % count_vowels(stmt)
