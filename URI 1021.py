valor = float(input())

nota100 = valor//100
valor -= nota100*100

nota50 = valor//50
valor -= nota50*50

nota20 = valor//20
valor -= nota20*20

nota10 = valor//10
valor -= nota10*10

nota5 = valor//5
valor -= nota5*5

nota2 = valor//2
valor -= nota2*2

moeda1real = valor//1
valor -= moeda1real

moeda50 = valor//0.5
valor -= moeda50*0.5

moeda25 = valor//0.25
valor -= moeda25*0.25

moeda10 = valor//0.10
valor -= moeda10*0.10

moeda5 = valor//0.05
valor -= moeda5*0.05

moeda1 = valor/0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %nota100)
print("%d nota(s) de R$ 50.00" %nota50)
print("%d nota(s) de R$ 20.00" %nota20)
print("%d nota(s) de R$ 10.00" %nota10)
print("%d nota(s) de R$ 5.00" %nota5)
print("%d nota(s) de R$ 2.00" %nota2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %moeda1real)
print("%d moeda(s) de R$ 0.50" %moeda50)
print("%d moeda(s) de R$ 0.25" %moeda25)
print("%d moeda(s) de R$ 0.10" %moeda10)
print("%d moeda(s) de R$ 0.05" %moeda5)
print("%d moeda(s) de R$ 0.01" %moeda1)