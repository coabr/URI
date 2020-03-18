# Read 3 floating-point numbers. After, print the roots of bhaskara’s formula.
# If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

if A == 0 or B**2-4*A*C < 0:
    print("Impossivel calcular")

else:
    R1 = (-B + (B**2-4*A*C)**(1/2))/(2*A)
    R2 = (-B - (B**2-4*A*C)**(1/2))/(2*A)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
