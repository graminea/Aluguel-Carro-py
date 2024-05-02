'''
#1
fut = {'a','b','h','j'}
vol = {'f','l', 't'}
nat = {'q', 'k', 'b'}
bas = {'y'}
continua = 'S'
while continua == 'S':
    print('1- Relação de alunos matriculados por modalidade')
    print('2- Matricular novos alunos')
    print('3- Alunos que tem direito ao desconto')
    print('4- Total de alunos que fazem cada modalidade e o total de alunos')
    n = int(input('Digite a opção desejada: '))
    if n < 1 or n > 4:
        print('valor fora da lista!!')
        n = int(input('Digite novamente: '))
    if n == 1:
        print(f'Alunos matriculados em futebol: ', ', '.join(fut))
        print(f'Alunos matriculados em volei: ', ', '.join(vol))
        print(f'Alunos matriculados em natação: ', ', '.join(nat))
        print(f'Alunos matriculados em basquete: ', ', '.join(bas))
    elif n == 2:
        print('Em qual modalidade você quer matricular?')
        print('1- Futebol, 2- Volei, 3- Natação, 4- Basquete')
        nova = int(input('Digite a modalidade: '))
        if nova < 1 or nova > 4:
            print('valor fora da lista!!')
            nova = int(input('Digite novamente: '))
        if nova == 1:
            fut.add(input('Digite o nome: '))
        elif nova == 2:
            vol.add(input('Digite o nome: '))
        elif nova == 3:
            nat.add(input('Digite o nome: '))
        elif nova == 4:
            bas.add(input('Digite o nome: '))
    elif n == 3:
        c = set()
        h = fut.intersection(vol)
        h1 = fut.intersection(nat)
        h2 = fut.intersection(bas)
        h3 = vol.intersection(nat)
        h4 = vol.intersection(bas)
        h5 = nat.intersection(bas)
        if len(h) >= 1:
            c.update(h)
        if len(h1) >= 1:
            c.update(h1)
        if len(h2) >= 1:
            c.update(h2)
        if len(h3) >= 1:
            c.update(h3)
        if len(h4) >= 1:
            c.update(h4)
        if len(h5) >= 1:
            c.update(h5)        
        print('Alunos com direito a desconto: ', ', '.join(c))
    elif n == 4:
        print(f' Número de alunos matriculados em futebol: {len(fut)}')
        print(f' Número de alunos matriculados em volei: {len(vol)}')
        print(f' Número de alunos matriculados em natação: {len(nat)}')
        print(f' Número de alunos matriculados em basquete: {len(bas)}')
        p = set()
        p.update(fut.union(vol)) 
        p.update(fut.union(bas))
        p.update(fut.union(nat))
        p.update(vol.union(bas))
        p.update(vol.union(nat))
        p.update(nat.union(bas))
        print(f'Total de Alunos: {len(p)}')
    continua = input('Deseja continuar? S/N: ').upper()
'''


'''
#2
empresa1 = {'a','b','h','j'}
empresa2 = {'f','l', 't', 'a', 'b'}
continua = 'S'
while continua == 'S':
    print('1- Relação de clientes de cada empresa')
    print('2- Cadastrar novos clientes')
    print('3- Clientes que tem direito ao desconto')
    print('4- Total de clientes que tem conta em cada empresa, relação de clientes que tem conta nas duas empresas e número total de clientes de ambas juntas: ')
    n = int(input('Digite a opção desejada: '))
    if n < 1 or n > 4:
        print('valor fora da lista!!')
        n = input('Digite novamente: ')
    if n == 1:
        print(f'Clientes da empresa1: ', ', '.join(empresa1))
        print(f'Clientes da empresa2: ', ', '.join(empresa2))
    elif n == 2:
        print('Em qual empresa voçê deseja cadastrar?')
        print('1- Empresa1, 2- Empresa2')
        nova = int(input('Digite o número: '))
        if nova < 1 or nova > 2:
            print('valor fora da lista!!')
            nova = int(input('Digite novamente: '))
        if nova == 1:
            empresa1.add(input('Digite o nome: '))
        else:
            empresa2.add(input('Digite o nome: '))
    elif n == 3:
        c = set()
        h = fut.intersection(vol)
        if len(h) >= 1:
            c.update(h)        
        print('Clientes cadastrados em ambas empresas: ', ', '.join(c))
    elif n == 4:
        print(f'Número de clientes da empresa1: {len(empresa1)}')
        print(f'Número de clientes da empresa2: {len(empresa2)}')
        print('Clientes de ambas as empresas: ', ', '.join(empresa1.union(empresa2)))
        print('Clientes pertencentes a apenas uma empresa: ',', '.join(empresa1.symmetric_difference(empresa2)))
        print(f'Número total de clientes: {len(empresa1.union(empresa2))}')
    continua = input('Deseja continuar? S/N: ').upper()
'''        
    
    

