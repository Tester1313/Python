#Thiago Henrique dos Santos
import datetime 
i = 0
aux = datetime.time(15,00,00)

while i < 8:
    c = str(input('Qual o tempo do competidor: '));
    d = c.split(':')
    b = datetime.time(00,int(d[0]),int(d[1]))
    
    if b < aux:
        aux = b
    i += 1
    
print('O vencedor foi o corredor de tempo: ',aux)


