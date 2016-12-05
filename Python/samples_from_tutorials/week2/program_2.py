'''
    Program to create D.S. for student database having 5 subjects
    and calculate percentage for each student.

    The student D.S. is of form
    {Name:[marks in each subject]}
'''
# pylint: disable=C0103

def get_marks(subject_number):
    ''' Get marks from the user for a particular subject '''
    print 'Enter marks for %d subject: ' %subject_number,
    return input()

def get_student_details(num_subjects):
    '''Function to get student name and marks from user
        and populate the student_list'''
    student_list = {}
    name = raw_input("Name of Student [Press 'Enter' to exit entry]: ")
    while len(name.strip()) > 0:
        print 'Enter marks for %d subjects for %s' % (num_subjects, name)
        student_list[name] = [get_marks(value) for value in range(1, num_subjects+1)]
        name = raw_input("Name of Student [Press 'Enter' to exit entry]: ")
    return student_list


def get_student_marks_total_and_percentage(student_list):
    '''Function to find the sum and percentage of all marks
       in the subjects for each student'''
    students_total_marks_and_percent = {}
    for each_student in student_list:
        total_marks = sum(student_list[each_student])
        total_subjects = len(student_list[each_student])
        percentage_marks = (float(total_marks)/(total_subjects*100)) * 100
        students_total_marks_and_percent[each_student] = (total_marks, percentage_marks)
    return students_total_marks_and_percent

def main():
    ''' Main function to be executed '''
    number_of_subjects = 5
    student_register = get_student_details(number_of_subjects)
    #print student_register
    total_marks_and_percentage = get_student_marks_total_and_percentage(student_register)
    print '*' * 80
    print ' ' * 5, 'Name:', ' ' * 25, 'Total Marks:', ' '*10, 'Percentage:'
    print '*' * 80
    for student in total_marks_and_percentage:
        print ' '*5, '%-30s' % student,     \
                     '%12d' % total_marks_and_percentage[student][0], ' '*14, \
                     '%8.2f' % total_marks_and_percentage[student][1]
    print '*'*80

#Execute main
main()
