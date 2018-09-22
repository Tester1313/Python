#Thiago Henrique dos Santos
resultado = []

def getBytesToMb(byte):
    return round(int(byte) * (10**-6),2)

def getPercentualUso(byte):
    soma = 0
    for linha in conteudo:
        valores = linha.split()
        soma += int(valores[1])

    return round((int(byte)*100)/soma,2)

def printRelatorio(resultado):
    writer.writelines(resultado)
    writer.close()

arquivo = open('C:\\usuarios.txt','r');
writer = open('C:\\teste\\relatorio.txt','w');

conteudo = arquivo.readlines()
resultado.append('ACME Inc.           Uso de espaço em disco pelos usuários \n')
resultado.append('--------------------------------------------------------------------- \n')
resultado.append("%s %-15s %-10s %15s"%('Nr. ',' Usuário','Espaço utilizado','% do Uso \n'))

i = 1
for linha in conteudo:
    valores = linha.split()
    resultado.append("%s %-22s %-15s %12s"%(str(i), str(valores[0]), str(getBytesToMb(valores[1])) +' MB',str(getPercentualUso(valores[1])) +' % \n'))
    i += 1

printRelatorio(resultado)
