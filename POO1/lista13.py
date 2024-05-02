
#1
lista1 = []
lista0 = []
q = int(input('Digite quantas pessoas participarão da pesquisa: '))
print('0- Satisfatório, 1- Não satisfeito')
for i in range(q):
    v = int(input(f'Digite a opinião do {i+1}º entrevistado: '))
    if v == 1:
        lista1.append(v)
    if v == 0:
        lista0.append(v)
if len(lista1)>=len(lista0):
    print('N')
elif len(lista1)<len(lista0):
    print('Y')



#2
n = int(input('Digite quantos casos teste: '))
for i in range(n):
    soma = 0
    q = int(input(f'Digite o {i+1}º número: '))
    for j in range(q-1,0,-1):
        if q % j == 0:
            soma += j
    if soma == q:
        print(f'{q} eh perfeito:')
    else:
        print(f'{q} nao eh perfeito')



#3
import random

n = int(input('Quantos jogos deseja fazer: '))
lista =[]
print('-=-=-=  SORTEANDO 4 JOGOS  -=-=-=')
for i in range(n):
    lista2 = []
    for j in range(5):
        lista2.append(random.randint(1,60))
    lista.append(lista2)
for p in range(n):
    print(lista[p])
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')



#4
q = int(input('Quantos alunos desejam cadatrar: '))
alunos = []
for i in range(q):
    aluno = []
    aluno.append(input('Digite o nome do aluno: '))
    for j in range(3):
        aluno.append(int(input(f'Digite a {j+1}º nota do aluno: ')))
    alunos.append(aluno)
print(alunos)

continua = 'S'
while continua == 'S':
    flag = False
    consulta = input('Qual aluno deseja consultar: ')
    for u in range(len(alunos)):
        if consulta in alunos[u]:
            media = (alunos[u][1] + alunos[u][2] + alunos[u][3]) / 3
            print(media)
            flag = True
    if flag == False:
        print('aluno não encontrado:')
        #continua = input('Deseja continuar? S/N: ').upper()
    continua = input('Deseja continuar? S/N').upper()



#5
while True:
soma = 4
n,m = map(int, input('Digite o número de participantes e o número de perguntas: ').split())
if n == 0 and m == 0:
    break
linha = [0] * n
matriz = [linha] * n

for i in range(n):
    linha = []
    for c in range(n):
        num = int(input('Digite se o {i}º aluno conseguiu resolver a {c}º questão: '))
        linha.append(num)
    matriz[i] = linha
if matriz[0][0] == 1 and matriz[0][1] == 1 and matriz[0][2] == 1 or matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[1][2] == 1 or matriz[2][0] == 1 and matriz[2][1] == 1 and matriz[2][2] == 1:
    soma += -1
if matriz[0][0] == 0 and matriz[1][0] == 0 and matriz[2][0] == 0 or matriz[0][1] == 0 and matriz[1][1] == 0 and matriz[2][1] == 0 or matriz[0][2] == 0 and matriz[1][2] == 0 and matriz[2][2] == 0:
    soma += -1
if matriz[0][0] == 1 and matriz[1][0] == 1 and matriz[2][0] == 1 or matriz[0][1] == 1  and matriz[1][1] == 1  and matriz[2][1] == 1 or matriz[0][2] == 1 and matriz[1][2] == 1 and matriz[2][2] == 1:
    soma += -1
if matriz[0][0] == 0 and matriz[0][1] == 0 and matriz[0][2] == 0 or matriz[0][0] == 0 and matriz[1][1] == 0 and matriz[1][2] == 0 or matriz[2][0] == 0 and matriz[2][1] == 0 and matriz[2][2] == 0:
    soma += -1
print(soma)



    
