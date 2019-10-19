codigo1, quantidade1, valor1 = (input()).split()

codigo2, quantidade2, valor2 = (input()).split()

produto_final = (float(quantidade1) * float(valor1))+(float(quantidade2) * float(valor2))

print ("VALOR A PAGAR: R$ %.2f" %produto_final)
