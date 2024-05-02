'''
#1
comandos = []
while True:
    n = int(input('Digite a quantidade de comandos dados pelo sargento: '))
    if n == 0:
        break
    comandos = input('Digite os comandos do sargento: ').strip().upper()
    direcao = 'N'
    for comando in comandos:
        if comando == 'E':
            if direcao == 'N':
                direcao = 'O'
            elif direcao == 'L':
                direcao = 'N'
            elif direcao == 'S':
                direcao = 'L'
            elif direcao == 'O':
                direcao = 'S'
        else:
            if direcao == 'N':
                direcao = 'L'
            elif direcao == 'L':
                direcao = 'S'
            elif direcao == 'S':
                direcao = 'O'
            elif direcao == 'O':
                direcao = 'N'
    print(direcao)
'''

'''
#2
n = int(input('Quantas verificações deseja fazer: '))
for i in range(n):
    lista = input('Digite:')
    if lista[0] == lista[2]:
        print(f'Números iguais!!! Produto dos números: {int(lista[0]) * int(lista[2])}')
    else:
        if lista[1].isupper():
            print(f'Dígito maiusculo!!! Diferença do primeiro e segundo números: {int(lista[2]) - int(lista[0])}')
        else:
            print(f'Dígito minúsculo!!! Soma do primeiro e segundo números: {int(lista[0]) + int(lista[2])}')
'''        

'''
#3
def verifica(x,y,z):
    while not(x<=y<=z):
            y = input('valor inválido, digite novamente: ')
            return y
    return str(y)
def verifica2(x,y,z):
    while not(x<=y<=z):
            y = input('valor inválido, digite novamente: ')
            return y
    return y
n = int(input('Digite o número de verificações: '))
n = verifica2(1,n,1000)
for i in range(int(n)):
    lista = input('Digite o número: ')
    lista = verifica(1,int(lista),(10**100))
    cont = 0
    for i in range(len(lista)):
        if lista[i] == '0':
            cont+=6
        elif lista[i] == '1':
            cont+=2
        elif lista[i] == '2':
            cont+=5
        elif lista[i] == '3':
            cont+=5
        elif lista[i] == '4':
            cont+=4
        elif lista[i] == '5':
            cont+=5
        elif lista[i] == '6':
            cont+=6
        elif lista[i] == '7':
            cont+=3
        elif lista[i] == '8':
            cont+=7
        elif lista[i] == '9':
            cont+=6
    print(cont)
'''


'''
#4
def verifica(x,y,z):
    while not(x<=y<=z):
        print('VALOR INCOMPATÍVEL')
        y = int(input('Digite novamente'))
    return y
soma = 0
somac = 0
somar = 0
somas = 0
n = int(input('Digite a quantidade de casos:'))
for i in range(n):
    Q = input(f'Digite o {i+1}º caso: ').strip().upper()
    Q = verifica(1,Q,15)
    if len(Q) == 4:
        if Q[3] == 'C':
            soma += int(Q[0])*10 + int(Q[1])
            somac += int(Q[0])*10 + int(Q[1])
        elif Q[3] == 'R':
            soma += int(Q[0])*10 + int(Q[1])
            somar += int(Q[0])*10 + int(Q[1])
        else:
            soma += int(Q[0])*10 + int(Q[1])
            somas += int(Q[0])*10 + int(Q[1])
    else:
        if Q[2] == 'C':
            soma += int(Q[0])
            somac += int(Q[0])
        elif Q[2] == 'R':
            soma += int(Q[0])
            somar += int(Q[0])
        else:
            soma += int(Q[0])
            somas += int(Q[0])
    

print(f'Total: {soma} cobaias')
print(f'Total de coelhos: {somac}')
print(f'Total de ratos: {somar}')
print(f'Total de sapos: {somas}')
print(f'porcentula de Coelhos: {round((somac/soma)*100 ,2)}%')
print(f'percentual de ratos: {round((somar/soma)*100 ,2)}%')
print(f'percentual de sapos: {round((somas/soma)*100 ,2)}%')
'''


'''
#5
def verifica(x,y,z):
    while not(x <= y <= z):
        print('VALOR INVALIDO')
        y = int(input('Digite novamente: '))
    return y
soma = 0
continua = 'S'
while continua == 'S':
    n = int(input('Digite o número de algarismos do número: '))
    n = verifica(1,n,10)
    m = input('Digite o número: ')
    if int(len(m)) != n:
        print('Número de algarismos diferente do número de algarismos previamente digitados.')
        m = input('Digite novamente: ')
    for i in range(len(m)):
        soma += int(m[i])
    if soma % 3 == 0:
        print(f'{soma} Sim')
    else:
        print(f'{soma} Não')
    continua = input('Deseja Continuar? S/N ').upper()
    soma = 0
'''

