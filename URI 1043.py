'''
Read three point floating values (A, B and C) and verify if is possible to make a triangle with them.
If it is possible, calculate the perimeter of the triangle and print the message:
Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:
Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.

'''

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if (a < b + c) and (a > abs(b)-abs(c)):
    if (b < a + c) and (b > abs(a)-abs(c)):
        if (c < b + a) and (c > abs(a)-abs(b)):
            perimetro = a+b+c
            print("Perimetro = %.1f" %perimetro)
else:
    area = ((a + b) *c)/2
    print("Area = %.1f" %area)