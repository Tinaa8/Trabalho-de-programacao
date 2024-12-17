alunos = []
professores = []
turmas = []
disciplinas = []

class Aluno:
    def __init__(self, nome: str, sobrenome: str, endereco: str, filiacao: str, email_responsavel: str, ra: str, segmento: str, curso: str, usuario: str, senha: str, turma=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.filiacao = filiacao
        self.email_responsavel = email_responsavel
        self.ra = ra
        self.segmento = segmento
        self.curso = curso
        self.turma = turma
        self.__usuario = usuario
        self.__senha = senha
        self._ativo = True

    @property 
    def usuario (self):
        return self.__usuario 
        
    @usuario.setter 
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha (self):
        return self.__senha
        
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
        
    def __str__(self):
        return f"Aluno: {self.nome} {self.sobrenome} | RA: {self.ra} | Segmento: {self.segmento} | Curso: {self.curso} | Ativo: {self._ativo}"

    def inserir_aluno(self):
        if self.segmento == "EM" and self.curso not in ["Mecatrônica", "Eletromecânica", "Informática"]:
            raise ValueError("Alunos do Ensino Médio devem estar associados a um curso válido.")
        elif self.segmento == "Superior" and self.curso not in ["Ciências da Computação", "Pedagogia"]:
            raise ValueError("Alunos do Ensino Superior devem estar associados a um curso válido.")
        alunos.append(self)

    def editar_aluno(self, **kwargs):
        for atributo, valor in kwargs.items():
            setattr(self, atributo, valor)

    def desativar(self):
        self._ativo = False

    def ativar(self):
        self._ativo = True

    def excluir_aluno(self):
        alunos.remove(self)

    def transferir_aluno(self, novo_curso):
        if self.segmento == "EM" and novo_curso not in ["Mecatrônica", "Eletromecânica", "Informática"]:
            raise ValueError("Transferência para um curso inválido no Ensino Médio.")
        if self.segmento == "Superior" and novo_curso not in ["Ciências da Computação", "Pedagogia"]:
            raise ValueError("Transferência para um curso inválido no Ensino Superior.")
        self.curso = novo_curso

class Professor:
    def __init__(self, nome: str, sobrenome: str, cpf: str, endereco: str, formacao: str, email: str, usuario: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.endereco = endereco
        self.formacao = formacao
        self.email = email
        self.__usuario = usuario
        self.__senha = senha
        self.disciplinas = []
        self.turmas = []
        self.segmentos = []
        self.ativo = True

    @property 
    def usuario (self):
        return self.__usuario 
        
    @usuario.setter 
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha (self):
        return self.__senha
        
    @senha.setter
    def senha(self, senha):
        self.__senha = senha    


    def __str__(self):
        return f"Professor: {self.nome} {self.sobrenome} | Formação: {self.formacao} | Ativo: {self.ativo}"

    def inserir_professor(self):
        professores.append(self)

    def editar_professor(self, **kwargs):
        for atributo, valor in kwargs.items():
            setattr(self, atributo, valor)

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def excluir_professor(self):
        professores.remove(self)

class Disciplina:
    def __init__(self, id: str, descricao: str, segmento: str, professor: Professor):
        self.id = id
        self.descricao = descricao
        self.segmento = segmento
        self.professor = professor
        self._ativa = True

    def __str__(self):
        return f"Disciplina: {self.descricao} | Código: {self.id} | Segmento: {self.segmento} | Professor: {self.professor}"

    def inserir_disciplina(self):
        disciplinas.append(self)

    def editar_disciplina(self, **kwargs):
        for atributo, valor in kwargs.items():
            setattr(self, atributo, valor)

    def desativar(self):
        self._ativa = False

    def ativar(self):
        self._ativa = True

    def excluir_disciplina(self):
        disciplinas.remove(self)

class Turma:
    def __init__(self, nome: str, segmento: str, ano: int, curso: str):
        self.nome = nome
        self.segmento = segmento
        self.ano = ano
        self.curso = curso
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self._ativa = True

    def __str__(self):
        return f"Turma: {self.nome} | Segmento: {self.segmento} | Ano: {self.ano} | Curso: {self.curso} | Alunos: {len(self.alunos)} | Ativa: {self._ativa}"

    def adicionar_aluno(self, aluno: Aluno):
        if aluno.segmento != self.segmento or aluno.curso != self.curso:
            raise ValueError("Aluno não compatível com a turma.")
        self.alunos.append(aluno)
        aluno.turma = self.nome

    def verificar_turma_valida(self):
        if self.segmento == "EM" and len(self.alunos) < 20:
            raise ValueError("Turma do Ensino Médio deve ter no mínimo 20 alunos.")
        if self.segmento == "Superior" and len(self.alunos) < 5:
            raise ValueError("Turma do Ensino Superior deve ter no mínimo 5 alunos.")

    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)

    def desativar(self):
        self._ativa = False

    def ativar(self):
        self._ativa = True

    def excluir_turma(self):
        turmas.remove(self)

def main():
    aluno1 = Aluno("William", "Silva", "Rua Alemães, 123", "Carlinhos Maia", "naosei1@email.com", "RA001", "EM", "Informática", "usuario1", "senha1")
    aluno1.inserir_aluno()

    aluno2 = Aluno("Maria", "Andrade", "Rua B, Bernardino", "Ana Banana", "naosei2@email.com", "RA002", "Superior", "Ciências da Computação", "usuario2", "senha2")
    aluno2.inserir_aluno()

    professor1 = Professor("Clara", "Escuro", "123.456.789-00", "Rua Das Dores, 789", "Mestre em Matemática", "clara@email.com", "clara.escuro", "senha123")
    professor1.inserir_professor()

    disciplina1 = Disciplina("D001", "Matemática", "EM", "Clara Escuro")
    disciplina1.inserir_disciplina()

    turma1 = Turma("Turma 1", "EM", 2024, "Informática")
    turma1.adicionar_aluno(aluno1)

    print(aluno1)
    print(professor1)
    print(disciplina1)
    print(turma1)

if __name__ == "__main__":
    main()