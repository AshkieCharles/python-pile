'''
My name is Ashkie Esperanza
May 04, 2023
The program must have a list and initialize 2 elements to the value of 0.
The program must give out the age and full name of the user.
'''

#This initializes the two elements in the lists to both have the value of '0'.

myList = [0,0]
name = input('Please enter your full name: ' , )

'''
Both have the int() prefix to be able to use that number to be added or subtracted.
We do not use float here as there are no decimals or fractions in a year or birth year.
'''

myList[0] = int(input('Please enter the current year: ' ,))

myList[1] = int(input('Please enter your birth year: ' ,))

age = (myList[0] - myList[1])


print("My name is {0},".format(name),'and I am', age,'years old.')

#The {0} pulls the name of the user that they have inputed.
