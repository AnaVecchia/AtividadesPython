class Carro:
    def __init__(self,marca,modelo,cor,combustivel, mensagem):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.mensagem = mensagem

        self.is_ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.is_ligado:
            print("veículo já esta ligado, sem alteracoes.")    
        else:
            self.is_ligado = True
            print("ligar veículo")

    def desligar(self):
        if self.is_ligado:
            self.is_ligado = False
            print("desligar veículo")
        else:
            print("veículo já esta desligado, sem alteracoes.")
            

    def acelerar(self):
        if self.is_ligado:
            self.velocidade += 1
            print(f"acelerando veículo: {self.velocidade}km/h")
        else:
            print("Ligue o veículo primeiro")

    def mensagem_para(self, conces, msg):
        conces.mensagem = msg
