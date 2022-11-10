from biblioteca import Biblioteca

livro_0 = Biblioteca("Ed e Lorrayne Warren")
livro_1 = Biblioteca("A Culpa é Das Estrelas")
livro_2 = Biblioteca("Vidas Secas")
livro_3 = Biblioteca("Para Todos os Garotos que Já Amei")
livro_4 = Biblioteca("Na Rota Do Perigo")
livro_5 = Biblioteca("A grota do lago")
livro_6 = Biblioteca("Os sete maridos de Evelyn Hugo")
livro_7 = Biblioteca("Do Mim ao Milhão")
livro_8 = Biblioteca("A coragem de ser imperfeito")
livro_9 = Biblioteca("O duque e eu")

print("Bem- vindo a biblioteca!")
cliente = input("Insira o seu nome para começarmos: ")
print(cliente,", escolha o livro que mais te atrai: \n 0 - Ed e Lorrayne Warren\n 1 - A Culpa é Das Estrelas\n 2 - Vidas Secas\n 3 - Para Todos os Garotos que Já Amei\n 4 - Na Rota Do Perigo\n 5 - A garota do lago\n 6 - Os sete maridos de Evelyn Hugo\n 7 - Do Mim ao Milhão\n 8 - A coragem de ser imperfeito\n 9 - O duque e eu")

selecao = int(input("Selecione o número do livro escolhido:"))

lista_livros = [livro_0, livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9]

opcao_sel = int(selecao)


for opcao in lista_livros:
    if opcao_sel >= 10:
        print("Infelizmente não foi encontrado este titulo, por favor, olhe s opções e escolha novamente..")
        break
    if opcao_sel <= 9:
        print(cliente,", seu livro ", lista_livros[opcao_sel].livro, "foi adicionada, obrigado pela preferência.")
        print("Volte sempre!!")
        break

