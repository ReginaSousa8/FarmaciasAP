import threading
class Stock:

    def __init__(self, idFarm, nome, quantidade):
        self.idFarm = idFarm
        self.nome = nome
        self.quantidade=quantidade
        self.lock=threading._RLock()
        self.condition=threading.Condition(self.lock)