from model.Pessoa import Pessoa

class Utente(Pessoa):

    def __init__(self,idUtente,nomeUtente, morada, nif, cc, tel):
        Pessoa.__init__(self,nomeUtente, morada, nif, cc, tel)
        self.idUtente = idUtente



