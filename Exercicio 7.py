#Thiago Henrique dos Santos

timeA = input("Informe o nome do time A: ")
timeB = input("informe o nome do time B: ")
time = timeA
placarA = 0
placarB = 0
pontos = 0

while time == timeA or time == timeB:
    time = input("Qual time realizou o arremesso ? ")
    
    if time != timeA and time != timeB:
        if placarA > placarB:
            print("O time vencedor foi: ", timeA)
        elif placarB > placarA:
            print("O time vencedor foi: ", timeB)
        else:
            print("O jogo ficou empatado")

        print ("Placar final: ",placarA, " X ",placarB)
        break;
    else:
        pontos = int(input("Cesta de quantos pontos: "))
        if pontos > 0:
            if pontos <= 3:
                if time == timeA:
                    placarA += pontos
                    print ("Placar: ", placarA, " X ", placarB)
                elif time == timeB:
                    placarB += pontos
                    print ("Placar: ", placarA, " X ", placarB)
            else:
                print("Os pontos não devem ser maior que 3, digite novamente")
        else:
            print ("Número invalido tente novamente")
        
