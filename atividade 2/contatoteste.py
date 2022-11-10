
from contato import Contato

contato_0 = Contato("Iuri", "969854128")
contato_1 = Contato("Eliedson", "940028922")
contato_2 = Contato("Jão", "903004040")
contato_3 = Contato("Francis", "99985003")
contato_4 = Contato("Maria Helena", "999964040")

print("Bem-vindo(a) à lista de contatos!")
cliente = input("Digite seu nome para começarmos: ")
print(cliente, "Sua lista é formada por esses contatos no momento: ", "\n [0]- ", contato_0.contato, "\n [1] - ", contato_1.contato,"\n [2] -", contato_2.contato,"\n [3] -", contato_3.contato, "\n [4] - ", contato_4.contato)

selecao = int(input("Selecione a opção desejada: "))

lista_contato = [contato_0, contato_1, contato_2, contato_3, contato_4]

opcao_sel = int(selecao)

for opcao in lista_contato:
    if opcao_sel >= 5:
        print("Sua opção está inválida, confira o número digitato!")
        break
    if opcao_sel <= 4:
        print(cliente, "o contato que você escolheu foi: ", lista_contato[opcao_sel].contato, "- Telefone:" , lista_contato[opcao_sel].telefone )
        print("Fale conosco novamente")
        break
