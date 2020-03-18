'''
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were 
positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).
'''

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C and D > A) and (C + D > A + B) and (C >= 0 and D >= 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
