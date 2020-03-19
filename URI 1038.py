'''
Using the following table, write a program that reads a code and the amount of an item. 
After, print the value to pay. This is a very simple program with the only intention of
 practice of selection commands.

code        specification         price
1           cachorro quente         4.00
2           x-salada                4.50
3           x-bacon                 5.0 
4           Torrada simples         2.0
5           Refrigerante            1.50


Input
The input file contains two integer numbers X and Y.
X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total 
value to be paid, with 2 digits after the decimal point.
'''


x, y = input().split()

x = float(x)
y = float(y)

price = 0

if x == 1:
    price = y * 4
elif x == 2:
    price = y * 4.5
elif x == 3:
    price = y * 5
elif x == 4:
    price = y * 2
elif x == 5:
    price = y * 1.5

print("Total: R$ %.2f" % price)
