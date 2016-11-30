# pylint: disable=C0103
'''
    Program to calculate gross salary from basic salary

    gross_salary = basic_salary + 10% DA + 12% TA)

    Test values
    Basic Salary        Gross Salary
    10.00               12.20
    50.00               61.00
    120.00              146.40

'''

basic_salary = input("Enter your basic salary: ")
d_allowance = (basic_salary * 10.0/100)
t_allowance = (basic_salary * 12.0/100)
gross_salary = basic_salary + d_allowance + t_allowance

print 'Your basic salary is %.2f and gross is %.2f' %(basic_salary, \
							gross_salary)
