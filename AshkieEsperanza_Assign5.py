'''
Ashkie Esperanza
June 1 2023
-Takes the story of Henry the square eared cat and turn it into Henry the pentagon eared cat
-Demonstrate your ability to manipulate, write to and delete a file
'''
import os

file = open('henryTheSquareEaredCat.txt', mode = 'r')

for line in file:
    print(line, end='')
    
newLines = []
for line in file:
    if 'square' in line:
        newLine = line.replace('pentagon')
        newLines.append(newLine)
    else:
        newLines.append(line)
file.close()

print(newLines)

file = open('henryThePentagonEaredCat.txt', mode = 'w')
for line in file:
    if 'square' in line:
        newLine = line.replace('pentagon')
        newLines.append(newLine)
    else:
        newLines.append(line)
newFile.close()
print(henryThePentagonEaredCat.txt)
