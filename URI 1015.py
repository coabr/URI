'''
x1, y1, x2 e y2 são os eixos de um avião, com os quais iremos calcular a distância entre eles 
'''
x1, y1 = input().split() 
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

print("%.4f" %distancia)