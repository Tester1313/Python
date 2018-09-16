# Thiago Henrique dos Santos

#modulo menus

def print_lista (opcoes):
    num = 1
    opcao = opcoes.split(';')
    for op in opcao:
        print (num, "-", op)
        num += 1
    opcao = int(input("Entre com a opção: "))
    return opcao

def menu_numerico (opcoes):
    opcao = print_lista(opcoes)
    while opcao <= 0 or opcao>len(opcoes):
        print ("Opcao invalida!")
        opcao = print_lista(opcoes)
    return opcao
