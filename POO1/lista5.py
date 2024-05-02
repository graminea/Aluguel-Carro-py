'''
#1113
while True:
    x, y = input(('Digite os dois valores separados por um espaço: ')).split()
    x = int(x)
    y = int(y)
    
    if x > y:
        print('Decrescente')     
    elif x < y:
        print('Crescente')
    else:
        break
'''

'''
#1099
soma = 0
while True:
    x, y = input(('Digite os dois valores separados por um espaço: ')).split()
    x = int(x)
    y = int(y)
    if x != 0:
        if x > y:
            x, y = y, x
        if x % 2 == 0:
            for i in range(x+1,y,2):
                soma = soma +  i
            print(soma)
        else:
            for i in range (x+2,y,2):
                soma = soma + i
            print(soma)
    soma = 0
'''



'''
#1021

n = float(input('Digite o valor a ser consultado: '))

cem = n // 100
cemresto = round (n % 100 ,2)

cinquenta = cemresto // 50
cinquentaresto = round (cemresto % 50 ,2)

vinte = cinquentaresto // 20
vinteresto = round (cinquentaresto % 20 ,2)

dez = vinteresto // 10
dezresto = round (vinteresto % 10 ,2)

cinco = dezresto // 5
cincoresto = round (dezresto % 5 ,2)

dois = cincoresto // 2
doisresto = round (cincoresto % 2 ,2)

um = doisresto // 1
umresto = round (doisresto % 1 ,2)

cinquentacents = umresto // 0.5
cinquentacentsresto = round (umresto % 0.5 ,2)

vintecincocents = cinquentacentsresto // 0.25
vintecincocentsresto = round (cinquentacentsresto % 0.25 ,2)

dezcents = vintecincocentsresto // 0.1
dezcentsresto = round (vintecincocentsresto % 0.1 ,2)

cincocents = dezcentsresto // 0.05
cincocentsresto = round (dezcentsresto % 0.05 ,2)

umcents = cincocentsresto * 100

print('NOTAS')
print(cem, 'notas de R$ 100,00')
print(cinquenta, 'notas de R$ 50.00')
print(vinte, 'notas de R$ 20.00')
print(dez, 'notas de R$ 10.00')
print(cinco, 'notas de R$ 5.00')
print(dois, 'notas de R$ 2.00')
print('MOEDAS')
print(um, 'moedas de R$ 1.00')
print(cinquentacents, 'moedas de R$ 0.50')
print(vintecincocents, 'moedas de R$ 0.25')
print(dezcents, 'moedas de R$ 0.10')
print(cincocents, 'moedas de R$ 0.05')
print(umcents, 'moedas de R$ 0.01')
'''


'''
#1247
d, vf , vg = input('Digite a distancia inicial entre a guarda e o ladrão, a velocidade do barco do ladrão e a velociade do barco da guarda: ').split()
d = int(d)
vf = int(vf)
vg = int(vg)

hip = ((12 ** 2) + (d ** 2))**(1/2)

if vf > vg or (hip / vg) > (12 / vf):
    print('N')
else:
    print('S')
'''


'''
#1708
cont = 1
x, y = input('Digite os tempos em segundo que os dois pilotos demoram para dar uma volta, separadas por um espaço: ').split()
x = int(x)
y = int(y)

if x > y:
    x, y = y, x

while x * cont >= y * (cont - 1):
    cont += 1
print(cont)
'''

'''
#2418
soma = 0
for i in range (5):
    nota = float(input('Digite a nota: '))
    if i == 0:
        maiornota = nota
        menornota = nota
    else:
        if nota > maiornota:
            maiornota = nota
        if nota < menornota:
            menornota = nota
    soma = soma + nota
soma = round(soma - maiornota - menornota ,1)
print(soma)
'''

'''
#2187
for n in range (1, 9999):
    while n < 100000:
        a = int(input('Digite o valor que deseja sacar: '))

        cinquenta = a // 50
        cinquentaresto = round (a % 50 ,2)

        dez = cinquentaresto // 10
        dezresto = round (cinquentaresto % 10 ,2)

        cinco = dezresto // 5
        cincoresto = round (dezresto % 5 ,2)

        um = cincoresto // 1
        umresto = round (cincoresto % 1 ,2)
        
        if a == 0:
            break

        print('teste', n)
        print(cinquenta, dez, cinco, um)
'''


'''
#1150
soma = 1
x = int(input('Digite o valor de x: '))
cont = x
while True:
    z = int(input('Digite o valor de z: '))
    if z < x:
        continue
    if z > x:
        break
    
while cont < z:
    cont += x + soma
    soma += 1
    
print(soma)
'''


'''
#2424
x, y = input('Digite as coordenadas x e y em que a bola caiu, separadas por uma vírgula: ').split(',')
                                                                                                
                                                                                                  
x = int(x)
y = int(y)

if x > 0 and x <= 432 and y > 0 and y <= 468:
    print('dentro')
else:
    print('fora')
'''


'''
#2454
print('0 = porta virada para esquerda')
print('1 = porta virada para direita')
p, r = input('Digite os valores das portas P e R, conforme a tabela acima, separados por um espaço: ').split()

p = int(p)
r = int(r)

if p == 0:
    print('C')
else:
    if r == 0:
        print('B')
    else:
        print('A')
'''


'''
#2373
n = int(input('Digite o número de bandejas: '))
soma = 0
for i in range(1, n+1):
    l , c = input(f'Digite o número de latas e copos, separados por um espaço, da tentativa {i}: ').split()
    
    l = int(l)
    c = int(c)
    
    if l > c:
        soma+= c
print(soma)
'''


'''
#1323
while True:
    n = int(input('Digite o número N que representa o numero de quadrados da lateral: '))
    soma = 0
    if n == 0:
        break
    else:
        for i in range(1, n+1):
            saida = i**2
            soma += saida
        print(soma)
'''      


'''
#2295
a, g, ra, rg = input('Digite o preço do alcool, da gasolina, a rendimento do carro a alcool e o rendimento a gasolina, todos separados por um espaço: ').split()
a = float(a)
g = float(g)
ra = float(ra)
rg = float(rg)

formula = round((g /a) ,2)
formula2 = round((rg / ra) ,2)
if (round(formula > formula2 ,2)):
    print('A') 
else:
    print('G')
'''


'''
#16
continua = 's'
while continua == 's':
    print('1 = Papel; 2 = Tesoura; 3 = Pedra')
    j1 = int(input('Jogador 1: Digite a opção desejada: '))
    j2 = int(input('Jogador 2: Digite a opção desejada: '))

    if j1 == 1 and j2 == 2:
        print('Jogador 2 venceu!!!')
    elif j1 == 1 and j2 == 3:
        print('Jogador 1 venceu!!!')
    elif j1 == 2 and j2 == 1:
        print('Jogador 1 venceu!!!')
    elif j1 == 2 and j2 == 3:
        print('Jogador 2 venceu!!!')
    elif j1 == 3 and j2 == 1:
        print('Jogador 2 venceu!!!')
    elif j1 == 3 and j2 == 2:
        print('Jogador 1 venceu!!!')
    elif j1 or j2 > 3:
        print('opção inválida')
    continua = input('Deseja Continuar? (s/n) ')
'''        
        

'''
#17

a, b, c = input('Digite os tres numeros separados por um espaço: ').split()
a= int(a)
b = int(b)
c = int(c)

if a > c:
    a, c = c, a
    
if a > b:
    a, b = b, a
    
if b > c:
    b, c = c, b
    
print(f' A ordem correta em ordem crescente é {a}, {b}, {c}')
'''




