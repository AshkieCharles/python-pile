'''
Loops in python
Ashkie Esperanza
May 22 2023
-Create a result similar to the 99 bottles of beer lyrics
-using loops
-use for loops

'''

for i in range(99, -1, -1):
    if i > 2:
        #The format adds the number that needs to be displayed on every lines of the beer bottle.
        print ('{} bottles of beer on the wall,\n{} bottles of beer!\nTake one down,\nPass it around,\n{} bottles of beer on the wall!\n\n'.format (i,i,i-1))
        #The \n {} code provides space and line break so that the sentence arent on the same lines.
    elif i == 2:
        #To make sure "bottles" is turned into "bottle".
        print ('{} bottles of beer on the wall,\n{} bottles of beer!\nTake one down,\nPass it around,\n1 more bottle of beer on the wall!\n\n'.format (i,i,))
        #"n1" adds the number 1
    elif i == 1:
        print ('1 bottle of beer on the wall,\n1 bottle of beer!\nTake it down,\nPass it around,\nNo more bottles of beer on the wall!')
print()
