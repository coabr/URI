a, b, c = input().split()
pi = 3.14159
a = float(a)
b = float(b)
c = float(c)
triangulo = (a*c)/2
area_circulo = pi*c**2
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b


print ("TRIANGULO: %.3f" %triangulo)
print ("CIRCULO: %.3f" %area_circulo)
print ("TRAPEZIO: %.3f" %trapezio)
print ("QUADRADO: %.3f" %quadrado)
print ("RETANGULO: %.3f" %retangulo)