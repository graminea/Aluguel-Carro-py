import sys
import time
from Login_e_Operacoes import Login_e_Operacoes
from Marcas import Carro, Marca, Ford, Chevrolet, Renault, Peugeot, Honda, Nissan, BMW, Citroen, Fiat
from utilidades import countdown


def menu_principal(login_e_operacoes_obj,marcas):
    while True:
        if login_e_operacoes_obj.logins[login_e_operacoes_obj.index_usuario_logado]["adm"]:
            print()
            print('LOGIN COMO ADIMINISTRADOR')
            print()
            print('\n--- Menu Principal ---')
            print('1. Adicionar Saldo')
            print('2. Consultar Saldo')
            print('3. Ver Catálogo')
            print('4. Alugar Carro')
            print('5. Encerrar o programa')
            print('6. Usuarios Logados')
            print('7. Adicionar carros')
            print('8. Mudar info de um carro')
        else:
            print('\n--- Menu Principal ---')
            print('1. Adicionar Saldo')
            print('2. Consultar Saldo')
            print('3. Ver Catálogo')
            print('4. Alugar Carro')
            print('5. Encerrar o programa')
            

        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            countdown(1)
            login_e_operacoes_obj.adcsaldo()
            countdown(3)

        elif opcao == 2:
            print('Verificando saldo.', end='')
            for i in range(2):
                print('.', end='', flush=True)
                countdown(1)
            login_e_operacoes_obj.verificarsaldo()
            countdown(3)

        elif opcao == 3:
            print('Gerando catálogo.', end='')
            for i in range(2):
                print('.', end='', flush=True)
                countdown(1)
            print('\n--- Catálogo de Carros ---')
            for marca in marcas:
                countdown(2)
                print(f"\n-- {marca.nome} --")
                for carro in marca.carros:
                    carro.imprimir_info()
            countdown(8)

        elif opcao == 4:
            print('Sistema de Aluguel conectado')
            countdown(1)
            login_e_operacoes_obj.alugar_carro(login_e_operacoes_obj,marcas)
            countdown(3)

        elif opcao == 5:
            print('ENCERRANDO O PROGRAMA.', end='')
            for i in range(2):
                print('.', end='', flush=True)
                countdown(1)
            sys.exit()
        
        elif opcao == 6:
            if login_e_operacoes_obj.logins[login_e_operacoes_obj.index_usuario_logado]["adm"]:
                login_e_operacoes_obj.get_logins('logins.json')
                print("Loaded logins:")
                countdown(1)
                for login in login_e_operacoes_obj.logins:
                    print(f"Usuario: {login['usuario']:<15} senha: {login['senha']:<15} saldo: R${login['saldo']}")
                countdown(3)
            else:
                print()
                print('Opção inválida. Tente novamente.')
                countdown(1)
                continue
        
        elif opcao == 7:
            if login_e_operacoes_obj.logins[login_e_operacoes_obj.index_usuario_logado]["adm"]:
                print()
                print('Entrando no sistema.', end='')
                for i in range(2):
                    print('.', end='', flush=True)
                    countdown(1)
                login_e_operacoes_obj.add_car(marcas)

        elif opcao == 8:
            if login_e_operacoes_obj.logins[login_e_operacoes_obj.index_usuario_logado]["adm"]:
                login_e_operacoes_obj.change_car(marcas)
                print('Info atualizada!!')
            countdown(1)

        else:
            print()
            print('Opção inválida. Tente novamente.')
            countdown(1)

ford_obj = Ford()
chevrolet_obj = Chevrolet()
renault_obj = Renault()
peugeot_obj = Peugeot()
chevrolet_obj = Chevrolet()
honda_obj = Honda()
nissan_obj = Nissan()
bmw_obj = BMW()
citroen_obj = Citroen()
fiat_obj = Fiat()


marcas = [ford_obj, chevrolet_obj,renault_obj, peugeot_obj, honda_obj, nissan_obj, bmw_obj, citroen_obj, fiat_obj]

login_e_operacoes_obj = Login_e_Operacoes()

while True:
    login_e_operacoes_obj.fazer_login()
    menu_principal(login_e_operacoes_obj,marcas)
    countdown(3)  

