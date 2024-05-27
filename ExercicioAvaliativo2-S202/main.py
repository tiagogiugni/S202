from database import Database
from databaseManager import TeacherCRUD

class CLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Criar um novo professor")
            print("2. Pesquisar um professor")
            print("3. Atualizar o CPF de um professor")
            print("4. Deletar um professor")
            print("5. Sair")
            choice = input("Digite o número da opção: ")
            
            if choice == '1':
                self.create_teacher()
            elif choice == '2':
                self.read_teacher()
            elif choice == '3':
                self.update_teacher()
            elif choice == '4':
                self.delete_teacher()
            elif choice == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_teacher(self):
        name = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o CPF do professor: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Professor criado com sucesso!")

    def read_teacher(self):
        name = input("Digite o nome do professor que deseja pesquisar: ")
        result = self.teacher_crud.read(name)
        print("Detalhes do Professor:", result)

    def update_teacher(self):
        name = input("Digite o nome do professor que deseja atualizar: ")
        new_cpf = input("Digite o novo CPF do professor: ")
        self.teacher_crud.update(name, new_cpf)
        print("CPF do professor atualizado com sucesso!")

    def delete_teacher(self):
        name = input("Digite o nome do professor que deseja deletar: ")
        self.teacher_crud.delete(name)
        print("Professor deletado com sucesso!")

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.195.0.185:7687", "neo4j", "implement-lump-workmen")
db.drop_all()

# Cria uma instância da classe TeacherCRUD para interagir com o banco de dados
school_db = TeacherCRUD(db)

# Cria um novo professor com as características fornecidas
school_db.create('Chris Lima', 1956, '189.052.396-66')
print("\nProfessor Chris Lima criado.\n")

# Pesquisa o professor com o nome "Chris Lima"
professor_details = school_db.read('Chris Lima')
print("\nDetalhes do Professor:\n")
for key, value in professor_details[0]['t'].items():
    print(f"{key}: {value}")

# Altera o CPF do professor "Chris Lima" para "162.052.777-77"
school_db.update('Chris Lima', '162.052.777-77')
print("\nCPF do professor Chris Lima alterado.\n")

# Pesquisa novamente para verificar a atualização
updated_professor_details = school_db.read('Chris Lima')
print("\nDetalhes Atualizados do Professor:\n")
for key, value in updated_professor_details[0]['t'].items():
    print(f"{key}: {value}")

# Cria uma instância da classe CLI para interagir com o usuário
cli = CLI(school_db)
cli.menu()

# Fechando a conexão com o banco de dados
db.close()