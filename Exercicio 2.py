#Thiago Henrique dos Santos

i = 1
count = 0
totalAprovado = 0
totalReprovado = 0
totalExame = 0
totalAlunos = 0

while i >= 0:
    num1 = int(input('Digite a nota do aluno:'))
    i = num1
    if i > 0:
        
        count += 1

        if num1 >= 70:
            totalAprovado += 1
        elif num1 < 30:
            totalReprovado += 1
        else:
            totalExame += 1
    
totalAlunos = totalAprovado + totalReprovado + totalExame;

if totalAlunos > 0:
    print ('Quantidade alunos aprovados ', totalAprovado,', percentual de: ', (totalAprovado*100)/totalAlunos)
    print ('Quantidade alunos de exame ', totalExame,', percentual de: ', (totalExame*100)/totalAlunos)
    print ('Quantidade alunos de reprovados ', totalReprovado,', percentual de: ', (totalReprovado*100)/totalAlunos)
else:
    print ('Nenhum aluno para realizar o calculo')
