from viagem import Viagem
viagem_0 = Viagem("Angra dos Reis")
viagem_1 = Viagem("Gramado")
viagem_2 = Viagem("Porto Velho")
viagem_3 = Viagem("Bahia")
viagem_4 = Viagem("Praia do Rosa")

print("olá \n muitas ofertas de viagem estão cheganddo, escolha uma das cidades mais belas do Brasil")
cliente = input("digite seu nome para comecarmos a fazer su cadastro dwe viagem")
print(cliente, "Temos opções de viagem otimaspara você! \n Angra dos Reis -[0] \n Gramado -[1]\n Porto Velho[2] \n bahia -[3] \n Praia do Rosa ")

selecao = int(input("Selecione o numero da cidade em que voce deseja ir viajar"))

lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4]

op_selecionada = int(selecao)

for lista in lista_viagem:
    if op_selecionada >= 5:
        print("opção deviagem indisponivel, tente outra opção.")
        break
    if op_selecionada <= 4:
        print(cliente, "sSua viagem já foi escolhido", lista_viagem[op_selecionada].cidade)
        break
