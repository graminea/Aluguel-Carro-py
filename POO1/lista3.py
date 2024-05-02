'''
#1
for i in range (2004, 2097, 4):
    print(i)
'''

'''
#2
for i in range (1, 50, 2):
    print(i)
'''

'''
#3
for i in range(5):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('digite a media: '))
    valor = float(input('Digite o valor da mensalidade: '))
    if i == 0:
        melhor = nota
        melhornome = nome
        melhorvalor = valor
    else:
        if (nota > melhor):
            melhornome = nome
            melhor = nota
            melhorvalor = valor
        
novamensalidade = melhorvalor - (melhorvalor * 0.3)
print('Aluno: ', melhornome)
print('Mensalidade: ', melhorvalor)
print('Nova mensalidade: ', novamensalidade)
'''

'''
#4
par = 0
impar = 0

for i in range (10):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('Pares = ', par)
print('Impares = ', impar)
'''


#5
tot = 0
num = int(input('Digite um numero: '))
for i in range(1, num+1):
    if (num % i == 0):
        tot += 1
if tot == 2:
    print('Primo')
else:
    print('Não é primo')


'''
#6
tot = 0
num = int(input('Digite um numero: '))
print('Divisivel por: ')
for i in range(2, num):
    if (num % i == 0):
        tot += 1
        print(i, end = ' ')
if tot == 0:
    print('Primo')
else:
    if tot != 0:
        print('\ne não é primo')
'''      


'''
#7
soma = 0
n = int(input('Digite quantas pessoas: '))
for i in range(n):
    idade = float(input('Digite a idade: '))
    soma = soma + idade
    
if (soma / n) < 26:
     print('turma Jovem')
if (soma / n) > 25 and (soma / n) < 60:
    print('Turma adulta')
if (soma / n) > 60:
    print('turma idosa')
'''

'''
#8
n= int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))

print('Números inteiros entre:', end=' ')

if n1 < n:
    n, n1 = n1, n
for intervalo in range(n + 1, n1 ):
    print(intervalo, end=' ')

soma = sum(range(n + 1, n1))


print("\n" 'Soma: ', soma)
'''
         

'''
#9
n = int(input('Digite o número inteiro que deseja fazer a tabuada: '))

if n < 1 or n > 10:
    print('Número não suportado')
else:
    print(f'Tabuada de {n}')
    for m in range(1, 11):
        resultado = n * m
        print(f'{n} x {m} = {resultado}')
'''


'''
#10
soma = 0
for i in range(5):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('digite a media: '))
    if i == 0:
        melhor = nota
        melhornome = nome
    else:
        if (nota > melhor):
            melhornome = nome
            melhor = nota
    soma = soma + nota
    
    if i == 0:
        n1 = nota
    elif i == 1:
        n2 = nota
    elif i == 2:
        n3 = nota
    elif i == 3:
        n4 = nota
    elif i == 4:
        n5 = nota
        
media = (soma) / 5

print('media: ', media)
        
print('Aluno: ', melhornome)

if melhor >= 5.75:
    print('Aprovado')
else:
    if melhor < 5.75 and melhor >= 2.75:
        print('Em recuperação')
    else:
        print('Reprovado')
'''

'''
#11
soma = 0
melhorn = 0
quantos = int(input('Digite quantos números deseja comparar: '))

for i in range(quantos):
    n = int(input('Digite o número: '))
    soma += n
    if i == 0:
        melhorn = n
    else:
        if n > melhorn:
            melhorn = n
        else:
            if n < melhorn:
                piorn = n
media = round(soma / quantos ,3)
print(f'Média: ', media)
print('Maior valor: ', melhorn)
print('Menor valor', piorn)
'''

'''
#12
conta2 = 0
conta = 0
p = int(input('Digite quantas praias quer cadastrar: '))

for i in range(1,p+1):
    nome = input('Digite o nome da praia: ')
    distancia = int(input('Digite a distancia do centro: '))
    conta += distancia
    if i == 1:
        maiordistancia = distancia
    else:
        if distancia > maiordistancia:
            maiordistancia = distancia
    media = conta / p
    if distancia > 14 and distancia < 21:
        conta2 = i

print(maiordistancia)
print(media)
print (conta2)
'''


        







    
    


