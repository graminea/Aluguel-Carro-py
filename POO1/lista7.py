'''
#1
def verifica(x,y ,z ):
    while not (x <= y <= z):
        y = int(input("DIGITE NOVAMENTE: "))
    return y

def jogo(a,b,c):
    if a == b and a != c and b != c:
        print('C')
    elif a == c and a != b and c != b:
        print('B')
    elif c == b and b != a and b != a:
        print('A')
    else:
        print('**')

while True:
    a = int(input('Digite o valor jogado por Alice: '))
    a = verifica(0, a, 1)
    b = int(input('Digite o valor jogado por Beto: '))
    b = verifica(0, b, 1)
    c = int(input('Digite o valor jogado por clara: '))
    c = verifica(0, c, 1)
    
    if a == 0 and b == 0 and c == 0:
        break
        
    jogo(a,b,c)
    
print()
'''


'''
#2
def verifica(x,y ,z,a):
    while not (x <= y <= z):
        if a > y:
            a,y = y,a
        y, a= (input("DIGITE NOVAMENTE: ")).split()
        y = int(y)
        a = int(a)
    return y
def periArea(x,y):
    perimetro = round((((x**2) + (y**2)) **(1/2))*2 ,0)
    area = round(x * (y/2) ,0)
    
    return perimetro,area
    

n = int(input('Digte o numero de pipas que serão construidas: '))

for i in range (n):
    x, y = input('Digite os valores de x e y: ').split()
    x = int(x)
    y = int(y)
    x = verifica(1,x,100,y)
    y = verifica(1,y,100,x)
    perimetro, area = periArea(x,y) 
    print(f'Área: {area} cm2   Perímetro: {perimetro} cm')
'''

'''
#3
def verifica(x,y ,z):
    while not (x <= y <= z):
        y = int(input("DIGITE NOVAMENTE: "))
    return y

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
for c in range(10):
    n = int(input('Digite o numero: '))
    n = verifica(2,n,301)
    p = verificaprimo(n)
    if p == 1:
        primo += 1
        
print(primo)
'''


'''
#4
def soma(inicio, fim):
    soma = 0
    for i in range(inicio,fim+1):
        soma += i
    return soma
    

def subtracao(minuendo,subtraendo):
    diminuamento = subtraendo - minuendo
    if minuendo > subtraendo:
        diminuamento = minuendo - subtraendo
    return diminuamento

continua = 's'
while continua == 's':
    x, y = (input('Digite o intervalo: ')).split()
    x = int(x)
    y = int(y)
    soma1 = soma(x,y)
    print(f'Soma do intervalo: {soma1}')
    
    a, b = input('Digite 2 valores: ').split()
    a = int(a)
    b = int(b)
    subtracao2 = subtracao(a,b)
    print(f'Diferença: {subtracao2}')
    continua = input('Deseja Continuar? (s/n) ')  
'''

'''
#5 ==> essa eu tentei por im tempão e não consegui professora, :C
def verifica(x,y,z):
    while not (x <= y <= z):
        y = int(input('DIGITE NOVAMENTE: '))
        return y
   
def multiplicaPrimos(a,b):
    p1=0
    p2=0
    while p1 == 0:  
        for i in range(a-1,0,-1):
                for k in range(1,i+1):                    
                    if (i % k == 0):
                        p1 += 1
                if p1 == 2:
                    p1 = i
                    break
                  
           
      
    
    while p2 == 0:                
        for j in range(b-1,0,-1):
            for l in range(1,j+1):
                if (b % l == 0):
                    p2 = j
                    break
                break
            break
        
    print(p1 * p2)             
    
    
x = int(input('Quantas verficações devem ser feitas: '))

for i in range(x):
    n, m = (input('Digite o primeiro valor: ')).split()
    n = int(n)
    m = int(m)

                   
    multiplicaPrimos(n,m)
'''

    




