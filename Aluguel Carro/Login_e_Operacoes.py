from utilidades import countdown
from Marcas import Carro, Marca, Ford, Chevrolet, Renault, Peugeot, Honda, Nissan, BMW, Citroen, Fiat
import json

class Login_e_Operacoes:
    def __init__(self):
        self.logins = []  
        self.usuarioslist = []
        self.oloco = 1  
        self.index_usuario_logado = None

        self.carregar_logins('logins.json')

    def fazer_login(self):
        while self.oloco == 1:
            print('\nBem Vindo a Sagás automóveis')
            h = input('Você tem cadastro na loja? (S/N): ').upper()
            if h == 'S':
                print('LOGIN.', end='')
                for i in range(2):
                    print('.', end='', flush=True)
                    countdown(1)
                
                usuario = input('\nDigite o usuário: ')
                senha = input('Digite a senha: ')
                for i in range(len(self.logins)):
                    if self.logins[i]['usuario'] == usuario and self.logins[i]['senha'] == senha:
                        self.usuario_logado = usuario
                        self.index_usuario_logado = i  
                        self.oloco = 0
                        print('Login efetuado com sucesso!!')
                        print('Entrando.', end='')
                        for i in range(2):
                            print('.', end='', flush=True)
                            countdown(1)
                        print()
                        break
                else:
                    print('Usuário ou senha incorretos!!')
                    print('Faça o login novamente!!')
                    print()
                    continue

            else:
                x = input('Deseja fazer o cadastro? (S/N): ').upper()
                if x == 'S':
                    self.loginscriar()

    def loginscriar(self):
        usuario = input('Crie um usuário: ')
        senha = input('Crie uma senha: ')
        self.logins.append({'usuario': usuario, 'senha': senha, 'saldo': 0})
        self.usuarioslist.append(usuario)
        print('Usuário criado com sucesso!')
        print('Realize o login para continuar.', end='')
        for _ in range(2):
            print('.', end='', flush=True)
            countdown(1)

        self.salvar_logins('logins.json')
        print()
        
    def adcsaldo(self):
        print()
        if self.usuario_logado is None:
            print('Você precisa estar logado para adicionar saldo.')
            return

        valor = float(input('Qual valor deseja adicionar?: '))
        countdown(2)
        print()
        print('Escolha a forma de pagamento:')
        print('1. Cartão de crédito')
        print('2. PIX')

        opcao_pagamento = int(input('Digite o número da forma de pagamento desejada: '))

        if opcao_pagamento == 1:
            self.adcsaldo_cartao(valor)
        elif opcao_pagamento == 2:
            self.adcsaldo_pix(valor)
        else:
            print('Opção inválida.')

    def adcsaldo_cartao(self, valor):
        print()
        print('Pagamento com cartão de crédito selecionado.')
        numero_cartao = input('Digite o número do cartão: ')
        nome_titular = input('Digite o nome do titular do cartão: ')
        codigo_seguranca = input('Digite o código de segurança do cartão: ')

        print(f'\nProcessando pagamento de R${valor:.2f} com o cartão de crédito...')
        countdown(3)
        self.atualizar_saldo2(valor)
        self.salvar_logins('logins.json')
        print('Pagamento realizado com sucesso!\n')

    def adcsaldo_pix(self, valor):
        print()
        print('Pagamento com PIX selecionado.')
        print('Gerando chave PIX.', end='')
        for i in range(2):
                print('.', end='', flush=True)
                countdown(1)
        print(f'\nEnvie PIX de R${valor:.2f} para a seguinte chave: pixsaldo@sagasautomoveis.com')
        input('Após realizar o PIX, pressione Enter para concluir o processo...')
        self.atualizar_saldo2(valor)
        self.salvar_logins('logins.json')
        print('Pagamento via PIX realizado com sucesso!\n')

    def verificarsaldo(self):
        if self.usuario_logado is not None:
            index_usuario_logado = self.usuarioslist.index(self.usuario_logado)
            print(f"\nSaldo em conta: R${self.logins[index_usuario_logado]['saldo']:.2f}")
        else:
            print('Você precisa estar logado para verificar o saldo.')
    
    def alugar_carro(self, login_e_operacoes_obj,marcas):
        print('\n--- Alugar Carro ---')
        print('Escolha a marca do carro que deseja alugar: ')
        for i, marca in enumerate(marcas, start=1):
            print(f"{i}. {marca.nome}")

        escolha_marca = int(input('Digite o número da marca: '))
        if 1 <= escolha_marca <= len(marcas):
            marca_escolhida = marcas[escolha_marca - 1]
            print(f'\n--- Carros da Marca {marca_escolhida.nome} ---')
            for i, carro in enumerate(marca_escolhida.carros, start=1):
                print(f"{i}. {carro.marca} {carro.modelo} ({carro.ano}) - R${carro.valor:,.2f} por dia")

            escolha_carro = int(input('Digite o número do carro que deseja alugar: '))
            if 1 <= escolha_carro <= len(marca_escolhida.carros):
                carro_comprado = marca_escolhida.carros[escolha_carro - 1]
                index_usuario_logado = login_e_operacoes_obj.usuarioslist.index(login_e_operacoes_obj.usuario_logado)
                
                print('DESCONTOS!')
                print('7 dias: 5% de desconto')
                print('14 dias: 10% de desconto')
                print('30+ dias: 20% de desconto')
                num_dias = int(input('Digite o número de dias que deseja alugar (mínimo 3): '))
                if num_dias < 3:
                    print('Número de dias inválido. Mínimo de 3 dias exigido.')
                    
                if num_dias >= 30:
                    desconto = 0.2  
                    print('Desconto aplicado: 20%')
                elif num_dias >= 14:
                    desconto = 0.1  
                    print('Desconto aplicado: 10%')
                elif num_dias >= 7:
                    desconto = 0.05  
                    print('Desconto aplicado: 5%')
                else:
                    desconto = 0  
                    print('Sem desconto aplicado.')

                valor_aluguel = carro_comprado.valor * num_dias * (1 - desconto)

                if login_e_operacoes_obj.logins[index_usuario_logado]['saldo'] >= valor_aluguel:
                    login_e_operacoes_obj.logins[index_usuario_logado]['saldo'] -= valor_aluguel
                    marca_escolhida.carros.pop(escolha_carro - 1)
                    self.salvar_logins('logins.json')
                    print(f'Valor da compra: R${valor_aluguel}')
                    input('Aperte enter para confirmar o valor e autorizar a transação...')
                    print(f'Carro alugado com sucesso! Saldo atualizado: R${login_e_operacoes_obj.logins[index_usuario_logado]["saldo"]:.2f}')
                else:
                    print('Saldo insuficiente para alugar este carro.')
            else:
                print('Escolha inválida.')
        else:
            print('Escolha inválida.')
    
    def get_logins(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                self.logins = json.load(nome_arquivo)
                self.usuarioslist = [login['usuario'] for login in self.logins]
        except FileNotFoundError:
            print('Arquivo JSON não encontrado')
    
    def atualizar_saldo2(self, valor):
        self.logins[self.index_usuario_logado]['saldo'] += valor

    def salvar_logins(self, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            json.dump(self.logins, file)

    def carregar_logins(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                self.logins = json.load(file)
                self.usuarioslist = [login['usuario'] for login in self.logins]
        except FileNotFoundError:
            print("Arquivo de logins não encontrado. Criando um novo.")
        

