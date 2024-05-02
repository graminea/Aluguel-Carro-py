#1
def preço(list,list2):
    soma = 0
    for l in range(len(list2)):
        for o in range(len(list)):
            if list2[l]['tipo'] in list[o]['tipo']:
                soma += float(list2[l]['valor']) * float(list[o]['valor'])
    return round(soma ,2)
        

tudo = {}
n = int(input('Digite a quantidade de vezes que Dona Percinova vai a feira: '))
for i in range(n):
    m = int(input('Digite a quantidade de produtos: '))
    list = []
    for j in range(m):
        tipo, valor = input(f'Digite a {j+1}º fruta/verdura: ').split()
        tudo['tipo'] = tipo
        tudo['valor'] = valor
        list.append(tudo.copy())
    p = int(input('Digite a quantidade de cada uma: '))
    list2 = []
    for k in range(p):
        tipo, valor = input('Digite a quantidade: ').split()
        tudo['tipo'] = tipo
        tudo['valor'] = valor
        list2.append(tudo.copy())            
    final = preço(list,list2)
    print(f' R$ {final}')
        


#2
def lingua(list,m):
    for j in range(len(list2)):
        for o in range(len(list)):
            if list2[j]['pais'] in list[o]['l']:
                print(list2[j]['nome'])
                print(list[o]['como'])
                print()

list = []
list2 = []
n = int(input('Digite a quantidade de linguas diferentes: '))
for i in range(n):
    linguas = {}
    linguas['l'] = input('Digite a lingua: ')
    linguas['como'] = input('digite como se escreve "Feliz Natal" naquela língua: ')
    list.append(linguas.copy())
m = int(input('Digite a quantidade de crianças que receberão as cartas: '))
for k in range(m):
    presentes = {}
    presentes['nome'] = input('Digite o nome: ')
    presentes['pais'] = input('Digite a nacionalidade: ')
    list2.append(presentes.copy())
lingua(list,m)



#3
def verificanomes(original, assinatura):
    diferenca = 0
    for i in range(len(original)):
        if original[i] != assinatura[i]:    
            diferenca += 1
    return diferenca

while True:
    N = int(input('Digite o número de alunos da sala: '))
    if N == 0:
        break

    originais = {}
    for _ in range(N):
        nome, assinatura = input('Digite o nome a assinatura Original: ').split()
        originais[nome] = assinatura

    M = int(input('Digite o número de presentes: '))
    assinaturas_falsas = 0

    for _ in range(M):
        nome, assinatura = input('Digite o nome e a assinatura da chamada: ').split()
        if nome in originais:
            diferenca = verificanomes(originais[nome], assinatura)
            if diferenca >= 1:
                assinaturas_falsas += 1

    print(assinaturas_falsas)



#4   
def verificalingua(a, b):
    if n in l:  
        print(l[n])
    else:
        print('Pais não encontrado!')
while True:
    l = {}
    l['brasil'] = 'Feliz Natal!'
    l['alemanha'] =  'Frohliche Weihnachten!'
    l['austria'] =  'Frohe Weihnacht!'
    l['coreia'] = 'Chuk Sung Tan!'
    l['espanha'] = 'Feliz Navidad!'
    l['grecia'] = 'Kala Christougena!'
    l['estados-unidos'] = 'Merry Christmas!'
    l['inglaterra'] = 'Merry Christmas!'
    l['australia'] = 'Merry Christmas!'
    l['portugal'] = 'Feliz Natal!'
    l['suecia'] = 'God Jul!'
    l['turquia'] = 'Mutlu Noeller'
    l['argentina'] = 'Feliz Navidad!'
    l['chile'] = 'Feliz Navidad!'
    l['mexico'] = 'Feliz Navidad!'
    l['antardida'] = 'Merry Christmas!'
    l['canada'] = 'Merry Christmas!'
    l['irlanda'] = 'Nollaig Shona Dhuit!'
    l['belgica'] = 'Zalig Kerstfeest!'
    l['italia'] = 'Buon Natale!'
    l['libia'] = 'Buon Natale!'
    l['siria'] = 'Milad Mubarak!'
    l['marrocos'] = 'Milad Mubarak!'
    l['japao'] = 'Merli Kurimasu!'

    n = input('Digite o nome do pais, se quiser parar digite "pare": ').lower()
    if n == 'pare':
        break
    else:
        verificalingua(l,n)
        


#5
def verifica_sozinho(a,b):
    for j in range(n):
        if lista.count(j) % 2 != 0:
            print(j)
while True:
    lista = []
    n  = int(input('Digite o número de números: '))
    if n == 0:
        break
    for i in range(n):
        lista.append(int(input('Digite: ')))
    verifica_sozinho(n,lista)



#6
def verifications(a,b):
    countEPR = 0
    countEHD = 0
    count = 0
    for j in range(len(lista)):
        if 'EPR' in lista[j]:
            countEPR += 1
        elif 'EHD' in lista[j]:
            countEHD += 1
        else:
            count += 1
    print(f'EPR: {countEPR}')
    print(f'EHD: {countEHD}')
    print(f'INTRUSOS: {count}')
    
lista = []
n = int(input('DIgite o número de alunos: '))
for i in range(n):
    alunos = {}
    matrícula, curso = input('Digite a matrícula e o curso: ').split()
    alunos[curso] = matrícula
    lista.append(alunos)
verifications(lista,n)




#7
def verificahay(cargos,descricao):
    salario = 0
    for palavra in descricao:
        if palavra in cargokeys:
            salario += cargos[palavra]
    return salario
cargos = {}

m,n = map(int,input('Digite o número de palavras chave do Hay Point e a quantidade de descrições de cargos: ').split())

for i in range(m):
    tipo,valor = input('Digite a função e o valor: ').split()
    cargos[tipo] = int(valor)
    cargokeys = list(cargos)
for l in range(n+2):
    descricao = input('Digite a descriçao: ').split()
    if descricao != ['.']:
        print(verificahay(cargos,descricao))
    else:
        continue
    



#8
n = int(input('Digite o número de pessoas participando do amigo secreto: '))
presentes = {}
for i in range(n):
    entrada = input('Digite o nome seguido das tres opções de presente: ').split()
    presentes[entrada[0]] = [entrada[1], entrada[2], entrada[3]]

for j in range(n+1):
    pessoa, presente = input('Digite o nome da pessoa e o presente que deseja consultar: ').split()
    if pessoa in presentes:
        if presente in presentes[pessoa]:
            print('Uhul! Seu amigo secreto vai adorar o/')
        else:
            print('Tente Novamente!')
    else:
        print('Tente Novamente!')



#9
def verifications(compasso,valoreskeys,valores):
    final = 0
    for d in compasso:
        total = 0
        for letra in d:
            if letra in valoreskeys:
                total += valores[letra]
        if total == 1:
            final += 1
    return final
valores = {'W' : 1 , 'H' : 1/2 , 'Q' : 1/4 , 'E': 1/8, 'S' : 1/16 , 'T' : 1/32, 'X': 1/64}
while True:
    compasso = input('digite os compassos: ').split('/')
    if compasso == ['*']:
        break
    valoreskeys = list(valores)
    print(verifications(compasso,valoreskeys,valores))


