# Criando uma classe Professor
class Professor:
  def _init_(self, nome):
    self.nome = nome

  def ministrar_aula(self, assunto):
    return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."

# Criando uma classe Aluno
class Aluno:
  def _init_(self, nome):
    self.nome = nome

  def presenca(self):
    return f"O aluno {self.nome} está presente."

# Criando uma classe Aula
class Aula:
  def _init_(self, professor, assunto):
    self.professor = professor
    self.assunto = assunto
    self.alunos = []

  def adicionar_aluno(self, aluno):
    self.alunos.append(aluno)

  def listar_presenca(self):
    mensagem = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
    for aluno in self.alunos:
      mensagem += f"- {aluno.nome}\n"
    return mensagem