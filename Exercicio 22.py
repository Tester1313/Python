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

def potencia(a,b):
    if b == 0:
        return 1
    else:
        return (a * potencia(a, b-1))

def fatorial(a):
    if a == 0:
        return 1
    else:
        return (a * fatorial(a-1))
    
def calcular(opcao,a,b):
    switcher = {
        1: soma(a,b),
        2: subtracao(a,b),
        3: multiplicacao(a,b),
        4: divisao(a,b),
        5: potencia(a,b),
        6: {fatorial(a), fatorial (b)}
    }
    print (switcher.get(int(opcao), 'Número invalido'))

opcao = menus.menu_numerico('Soma;Subtração (a-b);Multiplicação;Divisão (a/b , decimais);Potenciação (a^b);Fatorial de ambos;Inserir novos números;Sair')
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

calcular(opcao,a,b);

