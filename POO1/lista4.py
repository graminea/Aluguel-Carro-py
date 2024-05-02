'''
#1
while True:
    sexo = input('Digite seu sexo (M/F): ')
    if sexo != 'M' and sexo != 'F':
        print('!Tente novamente!')
    else:
       break
print('Ok')
'''     

'''
#2
from random import randrange
num = randrange (11)
cont = 1
teclado = int(input('Digite um numero ente 0 e 10: '))
while (num != teclado):
    teclado = int(input('Digite novamente: '))
    cont += 1
print('Parabens! Voce acertou! O numero secreto é {} \n Você fez {} tetativas'
      .format(num, cont))
'''

'''
#3
continua = 's'
while continua == 's':
    salario = float(input('Digite o salário: '))
    desconto = salario * .11
    if desconto <= 320:
        print(f'Desconto = R${desconto}')
    else:      
        print('Desconto maximo de R$ 320 atingido')
        print(f'Desconto em porcentagem ao salario, {(320 / salario) * 100: .2f}%')
    continua = input('Deseja Continuar? (s/n) ')
'''


'''
#4
#eia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
n = int(input('Digite o valor de n: '))
num = 1
while num < 10000:
    if num % n == 2:
        print(num)
    num += 1
'''


'''
#5
n = int(input('Digite o número inteiro que deseja fazer a tabuada: '))
x = 1
while x <= 10:
    print(f'{n} x {x} = {n * x}')
    x += 1
'''

'''
#6
i = True
while i:
    X = int(input('Digite a variavel: '))
    if X == 0:
        break
    cont = 1
    while cont <= X:
        if cont==X:
            print(cont,end="\n")
        else:
            print(cont,end=" ")
        cont += 1
'''


'''
#7
print('1.Alcool', '2.Gasolina', '3.Disel', '4. FIM')

gasolina = 0
alcool = 0
disel = 0

while True:
    entrada = int(input('Digite o combustivel segundo a tabela: '))
    if entrada == 1:
        gasolina += 1
    elif entrada == 2:
        alcool += 1
    elif entrada == 3:
        disel += 1
    elif entrada == 4:
        break
    else:
        print('Tente novamente')
print('Muito obrigado!')
print(f'Gasolina: {gasolina}')
print(f'Alcool: {alcool}')
print(f'Disel: {disel}')
'''


#8
maior = 0
menor = 0
cont = 0
while True:
    n, n2= (input('Digite dois números separados por um espaço: ')).split()
    n = int(n)
    n2 = int(n2)
    if n2 > n:
        n ,n2 = n2 ,n
    for i in range(n2, n+1):
        print(i, end=' ')
    if n2 <= 0 or n <= 0:
        break
    
    if n > n2:
        maior = n
        menor = n2
    else:
        maior = n2
        menor = n
    while maior <= menor :
        print(maior, end=' ')
        cont += maior
        maior+=1
print(f'sum = {cont}')
    
   

