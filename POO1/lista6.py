'''
#1
def contador(inicio, fim, passo):
    if fim > inicio:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
        print()
    else:
        for i in range(inicio, fim, -passo):
            print(i, end=" ")
        print()
    
contador(1, 10, 1)
contador(10, -1, 2)
x, y, z = input('Digite o inicio, o fim e o passo, seprados por um espaço: ').split()
x = int(x)
y = int(y)
z = int(z)
contador(x , y , z)
'''

'''
#2
def area(largura, comprimento):
    area = largura * comprimento
    print('Área = ', area)

largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: ' ))
area(largura,comprimento)
'''

'''
#3
def salarionovo(salario, novosalario, porcen, reajuste):
    if salario <= 400:
        novosalario = salario + (salario * 0.15)
        reajuste = novosalario - salario
        porcen = '15%'
    elif salario <= 800:
        novosalario = salario + (salario * .12)
        reajuste = novosalario - salario
        porcen = '12%'
    elif salario <= 1200:
        novosalario = salario + (salario * 0.10)
        reajuste = novosalario - salario
        porcen = '10%'
    elif salario <=2000:
        novosalario = salario + (salario * 0.07)
        reajuste = novosalario - salario
        porcen = '7%'
    else:
        novosalario = salario + (salario * 0.04)
        reajuste = novosalario - salario
        porcen = '4%'
    print(round(novosalario ,2))
    print(round(reajuste ,2))
    print(porcen)
    
novosalario = 0
reajuste = 0
porcen = 0
salario = float(input('Digite o salario: '))
salarionovo(salario,novosalario,reajuste,porcen)
'''

'''
#4
def horario(s, t, f):
    horario = s + t + f
    if s + t + f > 24:
        horario = horario - 24
    if s + t + f < 24:
        horario = horario + 24
    print(horario)
s, t, f = (input('Digite o horário de saida, o tempo da viagem e o tempo a mais ou a menos do novo fuso, separados por um espaço : ')).split()
s = int(s)
t = int(t)
f = int(f)
horario(s,t,f)
'''


'''
#5
def ultrapassa(soma, x , z , cont):   
    while cont < z:
        cont += x + soma
        soma += 1
    print(soma)
        
x = int(input('Digite o valor de x: '))
while True:
    z = int(input('Digite o valor de z: '))
    if z < x:
        continue
    if z > x:
        break
soma = 1
cont = x
ultrapassa(soma, x, z, cont)
'''


'''
#6
def quadrante(x , y):
        if x < 0 and y > 0:
            print('Segundo')
        elif x < 0 and y < 0:
            print('Terceiro')
        elif x > 0 and y < 0:
            print('Quarto')
        elif x > 0 and y > 0:
            print('Primeiro')
        
while True:     
    x,y = input('Digite as coordenadas separadas por um espaço: ').split()
    x = int(x)
    y = int(y)
    quadrante(x,y)
    if y == 0 or x == 0:
        break
'''


'''
#7
def elevador(c, n, e, s, soma, soma2, total):
    total = soma + soma2 
    if total > c:
        print('S')
    else:
        print('N')
n , c = input('Digite o número de leituras do leitor e a capacidade do mesmo: ').split()
n = int(n)
c = int(c)
soma = 0
soma2 = 0
total = 0
for i in range(n):
    s , e = input('Digite o numero de pessoas que sairam e que entraram: ').split()
    e = int(e)
    s = int(s)
    soma += e
    soma2 += -s
elevador(n , c , e , s, soma, soma2, total )
'''


'''
#1 com return
def colchao(a, b, c, h, l):
    if (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (b <= h and c <= l) or (b <= l and c <= h):
        return 'S'  # O colchão passa pelas portas
        print ('N')
    else:
        print ('S')
    return colchao
        
a, b, c = input('Digite as tres dimenções do colchão (altura, largura e comprimento, respectivamente) separadas por um espaço em branco: ').split()

a = int(a)
b = int(b)
c = int(c)

h, l = input('Digite a altura e a largura da porta, separadas por um espaço em branco: ').split()

h = int(h)
l = int(l)

recebacolchao = colchao(a,b,c,h,l)
if recebacolchao == 'S':
    print('Parabéns, você comporou o colchão ideal')
else:
    print('Compra outro que esse não passa kkkkkkj')
'''


'''
#2 com return
def alunos(a, melhornota, soma, media):
    for i in range(1, 6):
        a = int(input(f'Digite as médias do aluno {i}: '))
        soma += a
        if i == 1:
            melhornota = a
        else:
            if a > melhornota:
                melhornota = a
    media = soma / 5
    return media, melhornota
    
a = 0   
melhornota = 0
media = 0
soma = 0

media, melhornota = alunos(a, melhornota, soma, media)
if media < 2.75:
    print("reprovado")
else:
    if media >= 2.75 and media < 5.75:
        print('Em recuperção')
    else:
        if media > 5.74:
            print('Aprovado')
print(f'Melhor nota foi: {melhornota}')
'''


'''
#3 com return
def verifica(n, par, impar):
    if n % 2 == 0:
        print('Par')
        par += 1
    else:
        print('Impar')
        impar += 1
    return par, impar
par = 0
impar = 0
for i in range(10):
    n = int(input('Digite o numero: '))
    par, impar = verifica(n, par, impar)

print(f'Número de pares {par} e Número de impares {impar}')
'''


'''
#4 com return
def verificaprimo(n):
    tot = 0
    for i in range(1, n+1):
        if (n % i == 0):
            tot += 1
    if tot == 2:
        return 1
    else:
        return 0
        
primo = 0
x, y = input('Digite os valores do intervalo: ').split( )

x = int(x)
y = int(y)

if x > y:
    x , y = y ,x 

for c in range (x , y + 1):
    p = verificaprimo(c)
    if p == 1:
        primo += 1
print(primo)
'''


'''
#5 com return
def conta(media):
    media = soma / quantas
    return media
media = 0
quantas = 0
soma = 0
while True:
    x = int(input('Digite a idade: '))
    if x < 0:
        break
    else:
        soma += x
        quantas += 1
mediafinal = conta(media)
print(round(mediafinal ,2))
'''


'''
#6
def mediacao():
    media = z / soma
    return media , soma
soma = 0
z = 0
for i in range(6):
    x = float(input('Digite o número: '))
    if x > 0:
        soma += 1
        z += x
media, soma = mediacao()
print(f'{soma} valores positivos')
print(round(media ,2))
'''

'''
#7 com return
def verifica(Li, Ls, x):
    while not (Li <= x <= Ls):
        x = int(input("DIGITE NOVAMENTE: "))
    return x

def calcula_distância(t ,v):
    soma = t * v
    return soma
calcula = 0
n = int(input('Digite quantos intervalos de tempo: '))
n = verifica(1,10,n)

for i in range(n):
    t = int(input('Digite o tempo decorrido em horas: '))
    t = verifica(0,1000,t)

    v = int(input('Digite a velociade média no trecho: '))
    v = verifica(0,1000,v)
    
    calcula += calcula_distância(t ,v)

print(calcula)
'''





    
    
    




 