class Carro:
    def __init__(self, marca, modelo, ano, kilometragem, motor, cambio, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometragem = kilometragem
        self.motor = motor
        self.cambio = cambio
        self.valor = valor

    def imprimir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) -  {self.motor} - {self.cambio} - R${self.valor:,.2f} por dia")

class Marca:
    def __init__(self, nome, carros):
        self.nome = nome
        self.carros = carros


class Ford(Marca):
    def __init__(self):
        carros_ford = [
        Carro('FORD', 'New Fiesta', 2014, '126000km', 1.6, 'Manual', 60),
        Carro('FORD', 'Focus', 2015, '80000km', 2.0, 'PowerShift', 70), 
        Carro('FORD', 'Ford Ka', 2020, '61000km', 1.0, 'Manual', 65),
        Carro('FORD', 'Fiesta', 2008, '180000km', 1.6, 'Manual', 45),
        Carro('FORD', 'EcoSport', 2017, '100000km', 2.0, 'PowerShift', 65)
        ]
        Marca.__init__(self, 'FORD', carros_ford)


class Chevrolet(Marca):
    def __init__(self):
        carros_chevrolet = [
        Carro('CHEVROLET', 'Celta', 2013, '129000km', 1.0, 'manual', 40),
        Carro('CHEVROLET', 'Astra', 2007, '148000km', 2.0, 'manual', 39), 
        Carro('CHEVROLET', 'Zafira', 2002, '250000km', 2.0, 'automático', 20), 
        Carro('CHEVROLET', 'Tracker', 2021, '50000km', '1.2 Turbo', 'automático', 80), 
        Carro('CHEVROLET', 'Corsa', 2008, '180000km', 1.4, 'manual', 25000)
        ]
        Marca.__init__(self, 'CHEVROLET', carros_chevrolet)

class Renault(Marca):
    def __init__(self):
        carros_renault = [
        Carro('RENAULT', 'Sandero', 2019, '40000km', 1.6, 'Manual', 50),
        Carro('RENAULT', 'Kwid', 2020, '20000km', 1.0, 'Manual', 40),
        Carro('RENAULT', 'Duster', 2018, '60000km', 2.0, 'Automático', 60),
        Carro('RENAULT', 'Clio', 2015, '75000km', 1.2, 'Manual', 45)
        ]
        Marca.__init__(self, 'RENOUT', carros_renault)

class Peugeot(Marca):
    def __init__(self):
        carros_peugeot = [
        Carro('PEUGEOT', '208', 2021, '15000km', 1.6, 'Automático', 70),
        Carro('PEUGEOT', '2008', 2020, '25000km', 1.2, 'Automático', 75),
        Carro('PEUGEOT', '308', 2019, '35000km', 1.6, 'Manual', 65),
        Carro('PEUGEOT', '3008', 2018, '45000km', 2.0, 'Automático', 85)
        ]
        Marca.__init__(self, 'PEUGEOT', carros_peugeot)

class Honda(Marca):
    def __init__(self):
        carros_honda = [
        Carro('HONDA', 'Civic', 2021, '15000km', 1.5, 'CVT', 80),
        Carro('HONDA', 'HR-V', 2020, '25000km', 1.8, 'Automático', 75),
        Carro('HONDA', 'Fit', 2019, '35000km', 1.5, 'CVT', 70)
        ]
        Marca.__init__(self, 'HONDA', carros_honda)

class Nissan(Marca):
    def __init__(self):
        carros_nissan = [
        Carro('NISSAN', 'Versa', 2022, '10000km', 1.6, 'CVT', 65),
        Carro('NISSAN', 'Kicks', 2021, '20000km', 1.6, 'CVT', 70),
        Carro('NISSAN', 'Sentra', 2020, '30000km', 2.0, 'CVT', 75)
        ]
        Marca.__init__(self, 'NISSAN', carros_nissan)

class BMW(Marca):
    def __init__(self):
        carros_bmw = [
        Carro('BMW', '320i', 2022, '10000km', 2.0, 'Automático', 110),
        Carro('BMW', 'X3', 2021, '20000km', 2.5, 'Automático', 140),
        Carro('BMW', 'M2', 2020, '30000km', 3.0, 'Automático', 170)
        ]
        Marca.__init__(self, 'BMW', carros_bmw)

class Citroen(Marca):
    def __init__(self):
        carros_citroen = [
        Carro('CITROEN', 'C3', 2021, '15000km', 1.2, 'Automático', 55),
        Carro('CITROEN', 'C4 Picasso', 2020, '25000km', 1.6, 'Automático', 70),
        Carro('CITROEN', 'Aircross', 2019, '35000km', 1.6, 'Automático', 60)
        ]
        Marca.__init__(self, 'CITROEN', carros_citroen)

class Fiat(Marca):
    def __init__(self):
        carros_fiat = [
        Carro('FIAT', 'Palio', 2016, '110000km', 1.0, 'Manual', 40),
        Carro('FIAT', 'Toro', 2022, '15000km', 2.0, 'Automático', 90),
        Carro('FIAT', 'Punto', 2014, '130000km', 1.4, 'Manual', 50),
        Carro('FIAT', 'Uno', 2012, '139000km', 1.5, 'Manual', 35),
        Carro('FIAT', 'Argo', 2021, '19000km', 1.0, 'Manual', 70),
        Carro('FIAT', 'Marea', 1998, '137000km', '2.0 Turbo', 'Manual', 30)
        ]
        Marca.__init__(self, 'FIAT', carros_fiat)
