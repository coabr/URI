idade = int(input())

anos = idade//365

idade -= anos*365

meses = idade//30

idade -= meses*30

dias = idade

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)
