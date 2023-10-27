'''
Ashkie Esperanza
May 25 2023
-Use what we learned to create a pizza topping program
-ask the name of the customer
-list the toppings using 1-5
- 5 should have everything and must turn off the program alongside '0'
-add the total amount of money
    - 1 topping : 8
    - 2 topping : 10 
    - 3 topping : 12
    - 4 topping or everything : 14
-program must stop after 4 toppings have been chosen or at least 5 is chosen

'''


name = (input('Please enter a name: '))
#A dictionary with each number correesponding to a specific topping
toppings = {0: '', 1: 'Cheese', 2: 'Mushroom', 3: 'Pineapple', 4: 'Chicken'}
base_price = 6
#List initialized as zero and will contain the amount of toppings user has chosen
numberoftoppings = []
#Will place the corresponding dictionary key and pull the topping into the list
chosenTopping = []


print('Please select a topping (1-5) and 0 to exit')
print('1- Cheese \n2- Mushroom\n3- Pineapple\n4- Chicken\n5- Everything\n0- Exit')


#Prevents the program from executing more than 4 times by having a counter
i = 0
while i < 4:
    selection = int(input('>>>'))
    if selection == 5:
        #Adds the number into the empty list
        numberoftoppings.append(selection)
        #Adds all of the toppings into the list
        chosenTopping.append(toppings[1])
        chosenTopping.append(toppings[2])
        chosenTopping.append(toppings[3])
        chosenTopping.append(toppings[4])
        break
    elif selection == 0:
        break
    elif 0 < selection < 5:
        #If within 0 and 5 while not being equal to each, the program will run until it reaches 4 loops or until a user enters 0 or 5
        numberoftoppings.append(selection)
        chosenTopping.append(toppings[int(selection)])
        print('Please select a topping (1-5) and 0 to exit')
        print('1- Cheese \n2- Mushroom\n3- Pineapple\n4- Chicken\n5- Everything\n0- Exit')
        i += 1
    else:
        #If a number is chosen beyond 5 or lower than 0
        print('Invalid input! please try again')
        print('Please select a topping (1-5) and 0 to exit')
        print('1- Cheese \n2- Mushroom\n3- Pineapple\n4- Chicken\n5- Everything\n0- Exit')
        exit
#Calculates the total price    
price = base_price + 2*len(chosenTopping)
#If 5 or 0 is chosen in the beginning
if selection == 5:
    price = 14
    
if len(numberoftoppings) == 0:
    price = 0
print(f'Customer Name is {name}')
print(f'You selected: {chosenTopping}')
print(f'Your total is ${price}')
print('Have a wonderful day')
