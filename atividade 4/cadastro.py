class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome 
        self.periodo = periodo

class Alunos:
    def __init__(self, nome, matricula, periodo, curso):
        self.nome = nome
        self.matricula = matricula
        self.periodo = periodo
        self.curso = curso 
        
class Professor:
    def __init__(self, nome , materia, curso):
        self.nome = nome
        self.materia = materia
        self.curso = curso 
        
