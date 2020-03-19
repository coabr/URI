'''
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point,
 corresponding to 4 scores obtained by a student. Calculate the average with weights
  2, 3, 4 e 1 respectively, for these 4 scores and print the message "Media: " (Average),
   followed by the calculated result. If the average was 7.0 or more, print the message 
   "Aluno aprovado." (Approved Student). If the average was less than 5.0, print the message:
    "Aluno reprovado." (Reproved Student). If the average was between 5.0 and 6.9, including
     these, the program must print the message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed
 by the typed score. Recalculate the average (sum the exam score with the previous calculated
  average and divide by 2) and print the message “Aluno aprovado.” (Approved student) in case
   of average 5.0 or more) or "Aluno reprovado." (Reproved student) in case of average 4.9 or
    less. For these 2 cases (approved or reproved after the exam) print the message "Media final:
     " (Final average) followed by the final average for this student in the last line.

Input
The input contains four floating point numbers that represent the students' grades.

Output
Print all the answers with one digit after the decimal point.

'''

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
