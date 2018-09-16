#Thiago Henrique dos Santos

def numeroPorExtenso(num):
    aux = ''
    switcher = {
        1: 'Um',
        2: 'Dois',
        3: 'Três',
        4: 'Quatro',
        5: 'Cinco',
        6: 'Seis',
        7: 'Sete',
        8: 'Oito',
        9: 'Nove'
    }
    x=0
    number = str(abs(num))[::-1]
    while x < len(number):
        print (switcher.get(int(number[x]), 'Número invalido'))
        x +=1
        
print(numeroPorExtenso(234))
