## primeira questao
x = int(input("Digite um valor: "))
n = 1
while (n<10):
    print(x,'x',n,'=',n*x)
    n = n + 1
    
## segunda questao
A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda: "))
C = float(input("A terceira: "))

media = ((A*2)+(B*3)+(C*5))/3
print('Sua média é: {:.1f}'.format(media))

##terceira questao
A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda: "))

media = ((A*3.5)+(B*7.5))/2
print('media = {:5f}'.format(media))