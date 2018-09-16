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
    print (switcher.get(num, 'Número invalido'))
print(numeroPorExtenso(3))
