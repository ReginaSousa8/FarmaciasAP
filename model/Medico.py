from model.Pessoa import *

class Medico(Pessoa):
    
    def __init__(self, nomeMedico, morada, nif, cc, tel, especialidade):
        self.especialidade=especialidade
        Pessoa.__init__(self,nomeMedico, morada, nif, cc, tel)





