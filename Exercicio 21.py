#Thiago Henrique dos Santos

def pesoIdeal(altura,sexo):
    aux = 0
    if sexo == 0:
        aux = (72.7 * altura) - 58
    elif sexo == 1:
        aux = (62.1 * altura) - 44.7

    return aux
    
altura = float(input('Informe o altura da pessoa: '))
sexo = int(input('Informe o sexo da pessoa: '))
print('Peso ideal: ',pesoIdeal(altura,sexo))
