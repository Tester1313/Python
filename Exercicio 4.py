#Thiago Henrique dos Santos

i = 9
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
total = 0 

print('Para o candidato A vote 1')
print('Para o candidato B vote 2')
print('Para o candidato C vote 3')
print('Para o candidato D vote 4')
print('Nulo vote 5')
print('Branco vote 6')

while i != 0:
    voto = int(input('Informe o número do seu candidato:' ))
    i = voto

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        print ('Candidato não cadastrado')
        
total = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco
print('Total de votos do candidato 1 :', candidato1);
print('Total de votos do candidato 2 :', candidato2);
print('Total de votos do candidato 3 :', candidato3);
print('Total de votos do candidato 4 :', candidato4);
print('Total de votos nulos :', nulo, ' percentual de nulos :',(nulo*100)/total);
print('Total de votos brancos :', branco, 'percentual de brancos :',(branco*100)/total);

