#Thiago Henrique dos Santos
def get_input():
    input('''Entre com um texto: ''')
    lines = []
    count_line_break = 0
    while True:
        line = input()
        if not line:
            count_line_break = count_line_break + 1
        if count_line_break < 1:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return(str(text))



letra = input("Entre com uma letra: ")
frase = get_input()
cont = 0
posicao = ''
i=0
j = 0
linha = 1

while i<len(frase):
    if frase[i] == letra:
        cont +=1
        print(linha)
        posicao += str(i) + ', na linha ' + linha;
    elif frase[i] == '\n':
        linha += 1;
       
    i+=1
print (cont)
print ("Posicao das ocorrencias", posicao)
print ("Linhas com ocorrencias da letra", linha)



