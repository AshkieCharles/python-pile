'''This is a way to write multiple comments
This program will calcualte the area of a circle'''
#Step 1: Get the radius
#Use inp() to get user input
#Use float or integer so that it isn't considered as a string
radius = float(input("input the circle radius:" ))
#Step 2: Calculate the circle area
area = radius * radius * 3.14
#Step 3: Display the cricle area
#print('Circle Radius =' , radius)
#print("\nCircle Area = ",area)
#print('Circle Radius = {}\nCircle Area = {}'.format(radius,area))

#Formatted string
print(f'circle Radius = {radius}\nCircle Area = {area}')
