class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento
        
    def __str__(self):
        return f"{self.nome} (Doc: {self.documento})"

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __str__(self):
        return f"Nota: {self.nota}, Distância: {self.distancia}km, Valor: R${self.valor:.2f}, Passageiro: {self.passageiro}"  

class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.corridas = []
    
    def addCorrida(self, corrida):
        self.corridas.append(corrida)

    def __str__(self):
       corridas_info = "\n".join(str(corrida) for corrida in self.corridas)
       return f"Nome do Motorista: {self.nome}\nCorridas:\n{corridas_info}"