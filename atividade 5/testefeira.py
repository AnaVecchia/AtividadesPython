from feira import Feira

fruta_0 = Feira("Cherimoia ")
fruta_1 = Feira("Lichia ")
fruta_2 = Feira("Mangostão ")
fruta_3 = Feira("Pitaya")
fruta_4 = Feira("Rambutão ")
fruta_5 = Feira("Romã")
fruta_6 = Feira("Kino")

print("seja bem-vindo(A) a nossa feira de frutas mais exóticas do Brasil!")

cliente = input("Digite aqui seu nome, por favor: ")

print(cliente, ", no momento temos essas opções de frutas para você efetuar a compra: \n [0] - cherimoia \n [1] - lichia \n  [2] - mangostão \n [3] - pitaya \n [4] - rambutão \n [5] - romã\n [6] - kino")

selecao = int(input("Digite a opção desejada: "))

lista_feira = [fruta_0, fruta_1, fruta_2, fruta_3, fruta_4, fruta_5, fruta_6]

opcao_sel = int(selecao)

for opcao in lista_feira:
    if opcao_sel >= 7:
        print("Atenção! Opção inválida")
        break
    if opcao_sel <= 6:
        print(cliente, "a fruta que você escolheu foi:", lista_feira[opcao_sel].frutas)
        print("Obrigado, volte sempre")
        break
