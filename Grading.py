'''Write a program that:
-asks the user to enter a grade
-check if the grade is valid (0-100) or not
-displayt the letter grade (A+, A...) based on the following table
:grade >= 90 and grade grade <== 100 ---> A+
grade < 90 and grade grade <== 85 ---> B
grade < 85 and grade grade <== 70 ---> C
grade < 70 and grade grade <== 50 ---> D
'''

grade = float(input("Please enter a grade betweem 0 and 100: "))
if(grade >= 0 and grade <= 100):
    print('valid')
    if (grade >= 90 and grade <= 100):
        print('A+')
    elif (grade >= 85):
        print('B')
    elif (grade >= 70):
        print('C')
    elif (grade >= 50):
        print('D')
    else:
        print('F')
        

        

        
else:
    print('invalid grade')
