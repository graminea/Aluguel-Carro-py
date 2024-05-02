'''
#1
valorcasa = float(input('Digite o valor da casa ' ))
salario = float(input('Digite o seu salário '))
anos = float(input('Digite o tempo em meses que você pretende pagar '))

valorprestacao = (valorcasa / anos)

if valorprestacao > (salario * 0.3):
   print("Empréstimo negado bobão")
else:
    print("O valor da prestação é de R$", valorprestacao)
'''

'''
#2
metodos = ' Metodos de pagamento: à vista (digite 1); 1x no cartão (digite 2); 2x no cartão (digite 3); 3x ou mais no cartão (digite 4)'
print(metodos)
produto = float(input('Digite o valor do produto: '))
condicao = int(input('Método de pagamento = '))

if condicao == 1:
    print( 'Seu produto com 10% de desconto: ', produto * 0.9)
else:
    if condicao == 2:
        print ( 'Seu produto com 5% de desconto: ', produto * 0.95)
    else:
        if condicao == 3:
            print ('Valor: ', produto)
        else:
            print ('Valor com juros', produto * 1.2)
'''

'''
#3
peso = float(input("Digite seu peso: "))
altura = float(input('Digite sua altura em cm: '))

imc = round((peso * 10000) / (altura * altura) ,2)

if imc < 18.5:
    print(imc, 'Abaixo do peso')
else:
    if imc > 18.5 and imc < 25:
        print(imc, 'peso ideal')
    else:
        if imc > 25 and imc < 30:
            print(imc, 'sobrepeso')
        else:
            if imc > 30 and imc < 40:
                print(imc, 'obesidade')
            else:
                if imc > 40:
                    print(imc, 'obesidade morbida')
'''

'''
#4
nota = float(input('Digite sua priemira nota: '))
nota1 = float(input('Digite sua segunda nota: '))
nota2 = float(input('Digite sua terceira nota: '))

media = (nota1 + nota + nota2) / 3

if media < 5:
    print("reprovado")
else:
    if media > 5 and media < 7:
        print('Em recuperção')
    else:
        if media > 7:
            print('Aprovado')
'''

'''
#1051
salario = float(input('Digite seu salário: '))

if salario > 2000 and salario < 3000:
    imposto = ( (salario - 2000) * 0.08)
else:
    if salario > 3000 and salario < 4500:
        imposto = (1000 * 0.08) + (salario - 3000) * 0.18
    else:
        if salario > 4500:
            imposto = ((1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28))
        else:
            imposto = 0 
if imposto == 0:
    print('isento')
else:
    print(imposto)
'''

'''
#1061
dia1 = int(input('Digite o dia inicial: '))
hora1, minuto1, segundo1 = input('Digite o horário em horas, minutos e segundos, no formato h:m:s ').split(":")
                                                                                                        

hora1 = int(hora1)
minuto1 = int(minuto1)
segundo1 = int(segundo1)

dia2 = int(input('Digite o dia final: '))
hora2, minuto2, segundo2 = input('Digite a data final no mesmo modelo anterior ').split(":")

hora2 = int(hora2)
minuto2 = int(minuto2)
segundo2 = int(segundo2)

if hora2 >= hora1:
    horas = hora2 - hora1
else:
    horas = 24 - hora1 + hora2
if minuto2 >= minuto1:
    minutos = minuto2 - minuto1
else:
    minutos = 60 - minuto1 + minuto2
if segundo2 >= segundo1:
    segundos = segundo2 - segundo1
else:
    segundos = 60 - segundo1 + segundo2
if hora1 > hora2:
    dias = (dia2 - 1) - dia1
else:
    dias = dia2 - dia1
print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
'''

'''
#1050
ddd = int(input('Digite o DDD que você quer consultar: '))
          
if ddd == 61:
    print ('Brasilia')
elif ddd == 71:
    print ('Salvador')
elif ddd == 11:
    print ('São Paulo')
elif ddd == 21:
    print ('Rio de Janeiro')
elif ddd == 32:
    print ('Juiz de Fora')
elif ddd == 19:
    print ('Campinas')
elif ddd == 27:
    print ('Vitória')
elif ddd == 31:
    print ('Belo Horizonte')
elif ddd == 48:
    print ('Florianópolis')
else:
    print ('DDD não cadastrado')
'''

'''
#1052
mes = int(input('Digite o número do mês: ' ))

if mes == 1:
    print('january')
elif mes == 2 :
    print('february')
elif mes == 3 :
    print('march')
elif mes == 4:
    print('april')
elif mes == 5:
    print('may')
elif mes == 6:
    print('june')
elif mes == 7:
    print('july')
elif mes == 8:
    print('august')
elif mes == 9:
    print('september')
elif mes == 10:
    print('october')
elif mes == 11:
    print('november')
elif mes == 12:
    print('december')
else:
    print('Número inválido')
'''

'''
#1036

a, b, c = input('Digite as variáveis A, B e C, separadas por um espaço: ').split()

a = float(a)
b = float(b)
c = float(c)

if a == 0:
    print('Impossível Calcular')
elif (-b + (b**2 - (4 * a * c))) < 0:
    print ('Impossível Calcular')
else:
    formula = round((-b + (b**2 - (4 * a * c))** (1/2)) / (2 * a) ,5)
    formula1 = round((-b - (b**2 - (4 * a * c))** (1/2)) / (2 * a) ,5)
    print('R1 = ', formula)
    print('R2 = ', formula1)
'''

'''
#2408

a, b, c = input('Digite as pontuações em sequencia, separadas por um espaço: ').split()

a = int(a)
b = int(b)
c = int(c)

if a > b > c:
    print(b)
elif a > c > b:
    print(c)
elif c > a > b:
    print(a)
elif b > c > a:
    print(c)
elif c > b > a:
    print(b)
elif b > a > c:
    print (a)
'''

'''
#2417

cv, ce, cs, fv, fe, fs = input('Digite os números, com espaços entre si, na seguinte sequencia: o número de vitórias do Cormengo, o número de empates do Cormengo, o saldo de gols do Cormengo, o número de vitórias do Flaminthians, o número de empates do Flaminthians e o saldo de gols do Flaminthians. ').split() 

cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

saidac = (cv * 3) + ce
saidaf = (fv * 3) + fe

if saidac > saidaf:
    print ('C')
elif saidac < saidaf:
    print ('F')
elif saidac == saidaf and cs > fs:
    print ('C')
elif saidac == saidaf and cs < fs:
    print ('F')
else:
    print('=')
'''

'''
#2568

d, i, x, f = input('Digite o dia em que Ada registrou o preço da ação, o preço inicial da ação, a variação diária da ação e o número de dias que querem a previsão, separados por um espaço: ').split()

d = int(d)
i = int(i)
x = int(x)
f = int(f)

if d % 2 != 0 and (d + f) % 2 == 0:
    print(i + x)
else:
    if d % 2 == 0 and (d + f) % 2 != 0:
        print(i - x)
    else:
        if d % 2 != 0 and (d + f) % 2 != 0:
            print(i)
        else:
            if d % 2 == 0 and (d + f) % 2 == 0:
                print(i)
'''

'''
#2600

a = int(input('Digite o número da primeira face planificada: '))
b, c, d, e = input('Digte os números das faces planificadas do segundo segmento, com espaços em branco entre si: ').split()

b = int(b)
c = int(c)
d = int(d)
e = int(e)

f = int(input('Digite o número da ultima face planificada: '))

if a + f == 7 and b + d == 7 and c + e == 7:
    print('SIM')
else:
    print('NAO')
'''

'''
#1046

h1, h2 = input('Digite a hora de início e a final, com espaços em branco entre si: ').split()

h1 = int(h1)
h2 = int(h2)

if h1 < h2:
    horas = h2 - h1
else:
    horas = 24 - h1 + h2


print('O JOGO DUROU' ,horas, 'HORA(S)')
'''

'''
#1047

h1, m1, h2, m2 = input('Digite a hora e minutos iniciais e finais do jogo, separados por espaços: ').split()

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if h2 > h1:
    h3 = h2 - h1
if h2 > h1 and m1 > m2:
    h3 = (h2 - 1) - h1
else:
    h3 = 24 - h1 + h2
if m2 >= m1:
    m3 = m2 - m1
else:
    m3 = 60 - m1 + m2
    
print(f'O JOGO DUROU {h3} HORA(S) E {m3} MINUTO(S)')
'''

'''
#2375

bola = int(input('Digite o diâmetro da bola: '))
a, l, p = input('Digite a altura, a largura e a profundidade, respectivamente, da caixa, separadas por um espaço: ').split()

a = int(a)
l = int(l)
p = int(p)

if a >= bola and l >= bola and p >= bola:
    print ('S')
else:
    print ('N')
'''

'''
#1048
salario = float(input('Digite o salário: '))

if salario <= 400:
    novosalario = salario + (salario * 0.15) 
elif salario > 400 and salario <= 800:
    novosalario = salario + (salario * 0.12) 
elif salario > 800 and salario <= 1200:
    novosalario = salario + (salario * 0.10) 
elif salario > 1200 and salario <= 2000:
    novosalario = salario + (salario * 0.07)
else: 
    novosalario = salario + (salario * 0.04)

print(f'Novo salario: {novosalario: .2f}')
print (f'Reajuste ganho: {round(novosalario - salario):.2f}')

if salario <= 400:
    print('Reajuste em percentual: 15%')
elif salario > 400 and salario <= 800:
    print('Reajuste em percentual: 12%')
elif salario > 800 and salario <= 1200:
    print('Reajuste em percentual: 10%')
elif salario > 1200 and salario <= 2000:
    print('Reajuste em percentual: 7%')
else:
    print('Reajuste em percentual: 4%')
'''

'''
#2409
a, b, c = input('Digite as tres dimenções do colchão (altura, largura e comprimento, respectivamente) separadas por um espaço em branco: ').split()

a = int(a)
b = int(b)
c = int(c)

h, l = input('Digite a altura e a largura da porta, separadas por um espaço em branco: ').split()

h = int(h)
l = int(l)

if b > h:
    print ('N')
else:
    print ('S')
'''

'''
#1035

a, b, c, d = input('Digite as variáveis a, b, c e d, com espaços entre si: ').split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores não aceitos') 
'''

'''
#1038

print('CÓDIGO        ESPECIFICAÇÃO            PREÇO')
print('  1          Cachorro Quente          R$ 4.00')
print('  2          X - Salada               R$ 4.50')
print('  3          X - Bacon                R$ 5.00')
print('  4          Torrada Simples          R$ 2.00')
print('  5          Refrigirante             R$ 1.50')

menu = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5}

codigo, quantidade = (input('Digite o código do produto segundo a tabela acima, bem como a quantidade, separados por um espaço em branco: ')).split()

codigo = int(codigo)
quantidade = int(quantidade)

valor = menu[codigo]
final = valor * quantidade

print(f"Total: R$ {final: .2f}")
'''

'''
#2339

c, p, f = input('Digite, com um espaço entre as respostas, o número de competidores, a quantidade de folhas de papel e quantas folhas de papel cada competidor deve receber, respectivamente: ').split()

c = int(c)
p = int(p)
f = int(f)

if (c * f) <= p:
    print('S')
else:
    print('N')
'''

'''
#1045
a, b, c = input('Digite os valores de a, b e c separados por um espaço: ').split()

a = float(a)
b = float(b)
c = float(c)

lados = [a, b, c]
lados.sort(reverse = True)

a, b, c = lados 

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')
elif (a == b != c) or (c == b != a) or (a == c != b):
    print('TRIANGULO ISOSCELES')
'''
