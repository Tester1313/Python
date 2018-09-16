# Thiago Henrique dos Santos

import menus


def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b > 0:
        return a/b

def potenciacao(a,b):
    potencia = 1
    if b == 0:
        return potencia
    else:
        potencia = multiplicacao(potencia,a)
        b -= 1
        potencia += potenciacao(a,b)
        print(potencia)
        return potencia
    
def calcular(opcao,a,b):
    switcher = {
        1: soma(a,b),
        2: subtracao(a,b),
        3: multiplicacao(a,b),
        4: divisao(a,b),
        5: potenciacao(a,b)
    }
    print (switcher.get(int(opcao), 'Número invalido'))
potencia = 0
opcao = menus.menu_numerico('Soma;Subtração (a-b);Multiplicação;Divisão (a/b , decimais);Potenciação (a^b);Fatorial de ambos;Inserir novos números;Sair')
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

calcular(opcao,a,b);

