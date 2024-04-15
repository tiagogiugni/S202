from classes import Corrida, Motorista, Passageiro
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class MotoristaCLI:
    def __init__(self, motorista_model):
        self.commands = {}
        self.motorista_model = motorista_model

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        menu_options = {
            "1": ("Cadastrar novo condutor", self.createMotorista),
            "2": ("Consultar informações de um condutor", self.readMotorista),
            "3": ("Atualizar dados de um condutor", self.updateMotorista),
            "4": ("Remover um condutor do sistema", self.deleteMotorista),
            "5": ("Sair do programa", self.sair)
        }
        
        self.commands.update(menu_options)

        while True:
            # clear_screen()
            print("\n-- Menu Principal --")
            for key, (description, _) in menu_options.items():
                print(f"{key}. {description}")
            choice = input("Selecione uma opção pelo número: ")

            action = self.commands.get(choice)
            if action and callable(action[1]):
                action[1]()
            else:
                print("Opção inválida, por favor escolha um número do menu.")


    def createMotorista(self):
        nome_motorista = input("Insira o nome do motorista: ")
        passageiro = self.createPassageiro()
        corridas = self.createCorrida(passageiro)
        motorista = Motorista(nome_motorista)
        for corrida in corridas:
            motorista.addCorrida(corrida)
        self.motorista_model.createMotorista(motorista)

    def createPassageiro(self):
        nome = input("Insira o nome do passageiro: ")
        documento = input("Insira o documento do passageiro: ")
        return Passageiro(nome, documento)

    def createCorrida(self, passageiro):
        corridas = []
        while True:
            add_corrida = input("Gostaria de adicionar uma corrida? Digite 1 para sim e 2 para não: ")
            if add_corrida == "1":
                nota = float(input("Avaliação da corrida: "))
                distancia = float(input("Distância da corrida: "))
                valor = float(input("Valor da corrida: "))
                corridas.append(Corrida(nota, distancia, valor, passageiro))
            elif add_corrida == "2":
                break
            else:
                print("Escolha inválida. Por favor, digite apenas 1 ou 2.")
        return corridas

    def readMotorista(self):
        id = input("ID do Motorista: ")
        motorista = self.motorista_model.readMotorista(id)
        if motorista:
            print("Motorista: ")
            print(str(motorista))
        else:
            print("Motorista não encontrado.")

    def updateMotorista(self):
        motorista_id = input("ID do Motorista: ")
        motorista = self.motorista_model.readMotorista(motorista_id)
        if motorista:
            nome = input("Entre com um novo nome:")

            motorista = self.motorista_model.updateMotorista(motorista_id, nome)
        else:
            print("Motorista não encontrado.")

    def deleteMotorista(self):
        motorista_id = input("ID do Motorista: ")
        motorista = self.motorista_model.readMotorista(motorista_id)
        if motorista:
            self.motorista_model.deleteMotorista(motorista_id)
            print("Motorista deletado.")
        else:
            print("Motorista não encontrado.")

    def sair(self):
        confirm = input("Tem certeza que deseja sair? (s/n): ")
        if confirm.lower() == 's':
            print("Encerrando o programa. Até mais!")
            exit()
