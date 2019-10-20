valor = int(input())

quanto_falta = valor

nota100 = quanto_falta//100
quanto_falta -= (nota100 * 100)

nota50 = quanto_falta//50
quanto_falta -= (nota50 * 50)

nota20 = quanto_falta//20
quanto_falta -= (nota20 * 20)

nota10 = quanto_falta//10
quanto_falta -= (nota10 * 10)

nota5 = quanto_falta//5
quanto_falta -= (nota5 * 5)

nota2 = quanto_falta//2
quanto_falta -= (nota2 * 2)

nota1 = quanto_falta//1
quanto_falta -= (nota1 * 1)

print(valor)
print("%d nota(s) de R$ 100,00" %nota100)
print("%d nota(s) de R$ 50,00" %nota50)
print("%d nota(s) de R$ 20,00" %nota20)
print("%d nota(s) de R$ 10,00" %nota10)
print("%d nota(s) de R$ 5,00" %nota5)
print("%d nota(s) de R$ 2,00" %nota2)
print("%d nota(s) de R$ 1,00" %nota1)