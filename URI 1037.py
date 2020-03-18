'''
You must make a program that read a float-point number and print a message saying in which 
of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read 
number is less than zero or greather than 100, the program must print the message “Fora de 
intervalo” that means "Out of Interval".

The symbol '(' represents greather than. For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

'''

number = float(input())

if number < 0 or number > 100:
    print("Fora de intervalo")
elif number <= 25:
    print("Intervalo [0,25]")
elif number > 25 and number <= 50:
    print("Intervalo (25,50]")
elif number > 50 and number <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")