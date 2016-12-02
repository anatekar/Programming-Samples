'''
	Program to create D.S. for student database having 5 subjects
    and calculate percentage for each student
'''
# pylint: disable=C0103

def get_student_details(student_list, num_subjects):
    '''Function to get student details from user
        and populate the student_list'''
    name = raw_input("Name of Student [Press 'Enter' to exit entry]: ")
    while len(name.strip()) > 0:
        print 'Now Enter marks for each subject for %s' % name
        marks_in_subject = []
        for value in range(1, num_subjects+1):
            print 'Enter Marks for Subject %d: ' %value,
            marks = input("")
            marks_in_subject.append(marks)
        student_list[name] = marks_in_subject
        name = raw_input("Name of Student [Press 'Enter' to exit entry]: ")

def print_student_marks_sum(student_list):
    '''Function to print the sum of all marks in the subjects'''
    print '*' * 80
    print ' ' * 5, 'Name:', ' ' * 25, 'Total Marks:', ' '*10, 'Percentage:'
    print '*'*80
    for each_student in student_list:
        total_marks = 0
        for marks_in_each_subject in student_list[each_student]:
            total_marks += marks_in_each_subject
        total_subjects = len(student_list[each_student])
        percentage_marks = (float(total_marks)/(total_subjects*100)) * 100
        print ' '*5, '%-30s' %each_student,     \
                    '%12d' %total_marks, ' '*14, \
                    '%8.2f' %percentage_marks
    print '*'*80

student_register = {}
number_of_subjects = 2
get_student_details(student_register, number_of_subjects)
#print student_register
print_student_marks_sum(student_register)

