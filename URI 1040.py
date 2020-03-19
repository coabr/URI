n1, n2, n3, n4 = input().split()

n1 = float(n1)*2
n2 = float(n2)*3
n3 = float(n3)*4
n4 = float(n4)*1

media = (n1+n2+n3+n4)/10

if media >= 7.0:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif media < 5.0 and media >= 0.0:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" %nota_exame)
    media_final = (media+nota_exame)/2
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" %media_final)
    elif media_final < 5.0:
        print("Aluno reprovado.")
