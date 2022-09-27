class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
    
    def ligar(self):
        print("o "+self.modelo+"esta ligado")
    
    def acelerar(self):
        print("o"+self.modelo+" esta acelerando")
        
    def desligar(self):
        print("o"+self.modelo+" esta desligado")
