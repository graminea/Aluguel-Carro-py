#1
class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
        
    def getpreco(self):
        return self.preco
    
    def setpreco(self):
        self.preco = int(input('Digite o novo preço: '))

dados_livro = input('Digite o nome do livro, a quantidade de paginas, o autor e o preço (separados por vírgulas): ')
nome, qtdPaginas, autor, preco = map(str.strip, dados_livro.split(','))

p1 = Livro(nome, qtdPaginas, autor, preco)

x = int(input('Digite o que deseja fazer (1 para obter preço, 2 para definir novo preço): '))

if x == 1:
    preco = p1.getpreco()
    print(preco)
elif x == 2:
    p1.setpreco()
    print(f"Novo preço definido: {p1.preco}")
else:
    print("Opção inválida.")



#2
class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = int(tempoSemDormir)  # Convertendo para inteiro
    
    def estudar(self):
        tempoDeEstudo = int(input('Digite o tempo de estudo: '))
        self.tempoEstudo = tempoDeEstudo - self.tempoSemDormir
        return self.tempoEstudo
    
    def dormir(self):
        qtdHorasDeSono = int(input('Digite o tempo de sono: '))
        self.tempoSono = qtdHorasDeSono - self.tempoSemDormir
        return self.tempoSono
    
    def getTempoSemDormir(self):
        return self.tempoSemDormir


alunos = input('Digite o nome do aluno, o curso e tempo sem dormir, separados por vírgulas: ')
nome, curso, tempoSemDormir = map(str.strip, alunos.split(','))


p1 = Aluno(nome, curso, tempoSemDormir)


estudar = p1.estudar()
dormir = p1.dormir()
semDormir = p1.getTempoSemDormir()
print(f'Tempo sem dormir: {semDormir}')
print(f'Estudar: {estudar}')
print(f'Dormir: {dormir}')



#3
class Carro:
    def __init__(self,consumo):
        self.consumo = consumo
        self.quantidade = 0
    
    def andar(self,distancia):
        self.distancia = distancia
        
    def getGasolina(self):
        self.quantidade -= (int(self.distancia))/(int(self.litros))
        print(self.quantidade)
        
    def addGasolina(self,litros):
        self.litros = litros
        self.quantidade += int(litros)
    
meuCarro = Carro(int(input('Digite o consumo do veiculo: ')))

meuCarro.addGasolina((input('Digite o quanto de gasolina abastecerá: ')))
meuCarro.andar((input('Digite a distancia: ')))
meuCarro.getGasolina()



        