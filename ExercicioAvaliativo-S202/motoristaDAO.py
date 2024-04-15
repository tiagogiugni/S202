from bson import ObjectId
from classes import Corrida, Motorista, Passageiro
from bson import ObjectId, errors

class MotoristaDAO:
    def __init__(self, database):
        self.database = database
    
    def createMotorista(self, motorista):
        try:
            dadosMotorista = {
                "nome": motorista.nome,
                "corridas": []
            }

            for corrida in motorista.corridas:
                dadosCorrida = {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                }
                dadosMotorista["corridas"].append(dadosCorrida)

            self.database.collection.insert_one(dadosMotorista)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")

    def readMotorista(self, id: str):
        try:
            if not ObjectId.is_valid(id):
                print("ID fornecido não é válido.")
                return None
            print(f"Aguarde!! Estamos procurando por um motorista com o ID: {id}")
            dadosMotorista = self.database.collection.find_one({"_id": ObjectId(id)})
            if dadosMotorista:
                motorista = self.constructObjectMotorista(dadosMotorista)
                return motorista
            else:
                print("Motorista não encontrado.")
                return None
        except errors.InvalidId as e:
            print(f"Erro: O ID fornecido não é um ObjectId válido - {e}")
            return None
        except Exception as e:
            print(f"Erro desconhecido ao ler motorista: {e}")
            return None
    
    def updateMotorista(self, id: str, nome: str):
        try:
            novoMotorista = self.database.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome}})
            print("Motorista atualizado com sucesso!")
            return novoMotorista
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return None
    
    def deleteMotorista(self, id: str):
        try:
            self.database.collection.delete_one({"_id": ObjectId(id)})
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")

# Contruir dados do motorista
    def constructObjectMotorista(self, dadosMotorista):
        nome = dadosMotorista["nome"]
        motorista = Motorista(nome)
        for corrida_data in dadosMotorista.get("corridas", []):
            nota = corrida_data["nota"]
            distancia = corrida_data["distancia"]
            valor = corrida_data["valor"]
            dadosPassageiro = corrida_data["passageiro"]
            passageiro = Passageiro(dadosPassageiro["nome"], dadosPassageiro["documento"])
            corrida = Corrida(nota, distancia, valor, passageiro)
            motorista.addCorrida(corrida)
        return motorista