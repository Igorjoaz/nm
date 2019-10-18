## TABUADA
x = int(input())
n = 1                                      * LEMBRE-SE QUE A SAÍDA TEM QUE SER IGUAL A DO HUXLEY (CASO CONTRÁRIO NÃO ACEITA)
while (n<10):                              
    print(x,'X',n,'=',n*x)
    n = n + 1
    
## MEDIA 2 
A = float(input())
B = float(input())
C = float(input())

media = ((A*2)+(B*3)+(C*5))/10
print('MEDIA = {:.1f}'.format(media))   ou print('MEDIA = %.1f'%media)

## MEDIA 1 
A = float(input())
B = float(input())
media = ((A*3.5)+(B*7.5))/11
print('MEDIA = {:.5f}'.format(media)) ou print('MEDIA = %.5f'%media)

## BINGO 
x = int(input())
print('O numero sorteado foi:',x)

## ANTECESSOR E SUCESSOR 
num = int(input())
print(num-1,num+1)

## EXTREMAMENTE BASICO 
A = int(input())
B = int(input())
x = A + B
print('X =',x)

## COMABEM 
gasto = float(input())
total = (gasto * 0.1) + gasto 
print('{:.2f}'.format(total)) 

## AREA DO CIRCULO 
raio = float(input())
pi = 3.14159 
raio = (raio)/100   ( para transformar de cm em metro)
area = (raio**2)* pi
print('Area = {:.4f}'.format(area))

## DIFERENCA
A = int(input())
B = int(input())
C = int(input())
D = int(input())
x = A * B
y = C * D 
print('DIFERENCA =',x - y)

##SALARIO 
numero          = int(input())
trabalho_hrs    = int(input())
recebe_por_hora = float(input())
salario = trabalho_hrs * recebe_por_hora
print('NUMBER =',numero)
print('SALARY = R$ %.2f'%salario)


