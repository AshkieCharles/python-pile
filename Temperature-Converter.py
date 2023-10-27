'''
Ashkie Esperanza
May 12, 2023
Create a program that:
- take the user’s first name and the temperature in Celsius,
- use operators to perform a calculation
- A decision based on this calculation to return a string describing the temperature in fahrenheit
-If the Temperature (in Celsius):
• Is above 21 → print “<first name>, it is warm outside.”
• Is below 21 → print “<first name>, it is cool outside.”
• Is 21 → print “<first name>, it is perfect outside.”

'''

Name = input('Enter your first name: ' ,  )

celsius_temp = float(input('Enter temperature in celsius: ', ))

Fahrenheit = (1.8*celsius_temp) + 32
'''
This code makes sure that it is precise in its conversion and no excesses decimal
'''
Fahrenheit_rounded = round(Fahrenheit,1)

print(f'Temp in fahrenheit is {Fahrenheit_rounded}')

if (celsius_temp > 21):
    print(f'{Name}, It is warm outside')
elif (celsius_temp < 21):
    print(f'{Name}, It is cool outside')
else:
    print(f'{Name}, it is perfect outside')



