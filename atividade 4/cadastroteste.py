from cadastro import  Curso, Alunos, Professor

arquitetura = Curso("Arquitetura", "Integral")
direito = Curso("Direito", "Integral")
ads = Curso("Analise e Desenvolvimento de Sistemas", "Matinal")


aluno_eliedson = Alunos("Eliedson", "332556", "Integral",  arquitetura)
aluno_joão = Alunos("João", "569874","Integral", direito)
aluno_lucas = Alunos("Lucas","598321", "matinal", ads)

prof_marcio = Professor("Marcio","Ciencia politica", direito)
prof_maria = Professor ("Maria", "Análise e Gestão Ambiental", arquitetura)
prof_iuri = Professor("Iuri", "Programação", ads)

print(aluno_eliedson.curso.nome)
print(aluno_joão.curso.nome)
print(aluno_lucas.curso.nome)



