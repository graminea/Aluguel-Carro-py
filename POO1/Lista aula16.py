'''
#1
def verifica(x,y,z):
    while not(x<=y<=z):
        y = int(input('Digite novamente: '))
    return y
lista = []
lista2 = []
while True:
    n = int(input('Quantos casos teste: '))
    n = verifica(2,n,1000)
    if n == 0:
        break
    for i in range(n):
        lista.append(int(input(f'Digite o {i+1}º nível de suspeito: ')))
    for c in range(len(lista)):
        if c == 0:
            maior = lista[c]
        else:
            if lista[c] > maior:
                maior = lista[c]
    lista2 = lista[:]
    lista.remove(maior)
    for d in range(len(lista)):
        if d == 0:
            maior2 = lista[d]
        else:
            if lista[d] > maior2:
                maior2 = lista[d]
    print(lista2.index(maior2) + 1)
    lista.clear()
print('Fim')
'''

'''
#2
def verifica(x,y,z):
    while not(x<=y<=z):
        y = int(input('Digite novamente: '))
    return y
lista = []
dois = 0
tres = 0
quatro = 0
cinco = 0
n = int(input('Digite quantos números: '))
n = verifica(1,n,1000)
for i in range(n):
    lista.append(int(input(f'Digite o {i+1}º número: ')))
for c in range(len(lista)):
    if (lista[c] % 2) == 0:
        dois += 1
    if (lista[c] % 3) == 0:
        tres += 1
    if (lista[c] % 4) == 0:
        quatro += 1
    if (lista[c] % 5) == 0:
        cinco += 1
print(f'{dois} Multiplo(s) de 2')
print(f'{tres} Multiplo(s) de 3')
print(f'{quatro} Multiplo(s) de 4')
print(f'{cinco} Multiplo(s) de 5')
'''


'''
#3
def verifica(x,y,z):
    while not(x<=y<=z):
        print('NÚMERO NÃO SUPORTADO!!!')
        y = int(input('Digite novamente: '))
    return y
lista = []
lista2 = []
n = int(input('Digite o número de mergulhadores: '))
r = int(input('Digite o número de merlgulhadores que voltaram: '))
r = verifica(1,r,n)
n = verifica(r,n,10**4)
if r == n:
    print('*')
else: 
    for i in range(r):
        lista.append(int(input(f'Digite o número do {i+1}º mergulhador que voltou: ')))
    for c in range(n):
        if c+1 not in lista:
            lista2.append(c+1)
    print(*lista2, sep = ' ')
'''


'''
#4
def verifica(x,y,z):
    while not(x<=y<=z):
        print('VALOR NÃO SUPORTADO')
        y = int(input('Digite novamente: '))
    return y
def pulo(x):
    for c in range(len(x)):
        if x[c] >= n-1:
            if x[c+1] > x[c] + p:
                return False
            else:
                return True
lista = []
p, n = (input('Digite a altura do pulo do sapo e o número de canos: ')).split()
p = int(p)
p = verifica(1,p,5)
n = int(n)
n = verifica(2,n,100)
for i in range(n):
    lista.append(int(input(f'Digite a altura do {i+1}º cano: ')))
pulos = pulo(lista)
if pulos == True:
    print('YOU WIN')
else:
    print('GAME OVER')
'''


'''
#5
def verifica(x,y,z):
    while not(x<=y<=z):
        print('VALOR NÃO SUPORTADO')
        y = int(input('Digite novamente: '))
    return y
lista = []
n = int(input('Digite o número de casos: '))
n = verifica(2,n,100)
for i in range(n-1):
    lista.append(int(input(f'Digite o {i+1}º número: ')))
for c in range(1,n+1):
    if c not in lista:
        print(c)
'''