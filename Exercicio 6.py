#Thiago Henrique dos Santos

nota = 0
nome = ''
maiorNotaM = 0
maiorNotaF = 0
nomeMaiorM = ''
nomeMaiorF = ''
sexo = ''
countM = 0
countF = 0
somaF = 0
somaM = 0
total = 0
n = 0

totalM = 0
totalF = 0

while n < 4:
    nome = str(input('Digite o nome do aluno: '))
    nota = int(input('Digite a nota: '))
    sexo = str(input('Digite o sexo do aluno M ou F: '))

    if sexo == 'M':
        countM += 1
        somaM += nota
        if nota > maiorNotaM:
            maiorNotaM = nota
            nomeMaiorM = nome
    elif sexo == 'F':
        countF += 1
        somaF += nota
        if nota > maiorNotaF:
            maiorNotaF = nota
            nomeMaiorF = nome
    n += 1

total = countM + countF

print('Percentual de mulheres: ', (countF * 100)/total)
print('Percentual de homens: ', (countM * 100)/total)
print('Maior nota entre as mulheres: ', nomeMaiorF)
print('Maior nota entre os homens: ', nomeMaiorM)
print('Média das notas entre homens: ', somaM/countM)
print('Média das notas entre mulheres: ', somaF/countF)
