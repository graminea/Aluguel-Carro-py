import sys
import time
from Login_e_Operacoes import Login_e_Operacoes
from Marcas import Carro, Marca, Ford, Chevrolet, Renault, Peugeot, Honda, Nissan, BMW, Citroen, Fiat
from utilidades import countdown



def menu_principal(login_e_operacoes_obj,marcas):
    while True:
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

        else:
            print('Opção inválida. Tente novamente.')

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

