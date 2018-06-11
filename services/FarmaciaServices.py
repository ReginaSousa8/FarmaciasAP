# -*- coding: utf-8 -*-
from manager.ManagerFarmacia import ManagerFarmacia

class FarmaciaServices:

    def __init__(self):
        self.manager = ManagerFarmacia()

    def listaFarmacias(self):
        try:
            content = []
            content =  self.manager.GetFarmacias()
            if len(content) == 0:
                info = {}
                info["Farmacia Id"] = ""
                info["Nome"] = ""
                info["Morada"] = ""
            return content         
        except Exception as ex:
            raise Exception(ex)

    def adicionarFarmacia(self,idfarm,nome,morada):
        try:
            self.manager.CreateFarmacia(int(idfarm),nome,morada)
        except Exception as ex:
            raise Exception(ex)
        
    def SaveInfoDataBase(self):
        self.manager.SaveDataBaseOut()

# ---------------------------------------------Receitas---------------------------------------------------------------

    def RegistarReceita(self, idFarmacia, idReceita, idUtente, nomeMedico, listMedicamentos):
        if self.manager.ExisteFarmacia(idFarmacia) == None:
            raise Exception("Não existe farmacia no sistema")
        result = self.manager.ValidarMedicamentos(listMedicamentos)
        if len(result) > 0:
            result = self.manager.InsertReceita(int(idFarmacia),int(idReceita),int(idUtente), nomeMedico, listMedicamentos)
        print(result)

    def UpdateStock(self, idFarmacia, nomeMedic, quantidade):
        self.manager.UpdateStock(int(idFarmacia), nomeMedic, quantidade)

    def listarReceitas(self,idFarm):
        return self.manager.ListarReceitas(int(idFarm))

#------------------------------------------------Utentes-------------------------------------------------------------

    def adicionarUtente(self,idUtente,nomeUtente, morada, nif, cc, tel):
        self.manager.AddUtente(int(idUtente),nomeUtente, morada, nif, cc, tel)

    def updateUtente(self,idUtente,nomeUtente, morada, nif, cc, tel):
        self.manager.UpdateUtente(int(idUtente),nomeUtente, morada, nif, cc, tel)

    def apagarUtente(self,idUtente):
        self.manager.DeleteUtente(int(idUtente))

    def selectUtente(self,idUtente):
        return self.manager.GetUtente(int(idUtente))

    def listUtentes(self):
        try:
            content =  self.manager.GetUtentes()
            return content
        except Exception as ex:
            raise Exception(ex)

    def UtentesMaisReceitas(self):
        return self.manager.UtentesMaisReceitas()

    def MediaReceitaPorUtente(self,idUtente):
        return self.manager.MediaReceitaPorUtente(int(idUtente))

    def UtentesGastadores(self):
        return self.manager.UtentesGastadores()


#--------------------------------------------------Medicamentos------------------------------------------------------

    def AddMedicamento(self,nome, dosagem):
        self.manager.AddMedicamento(nome, dosagem)

    def listMedicamentos(self):
        val=self.manager.GetMedicamentos()
        return val

    def listMedicamentosStock(self,idfarm):
        val=self.manager.ListMedicamentoStock(idfarm)
        return val

    def MedicamentosAlarme(self,idfarm):
        return self.manager.MedicamentosAlarme(idfarm)

    def VerificarAlarme(self,ifdfarm):
        return self.manager.AlarmeMedicamentos(ifdfarm)

    def MedicamentosMaisVendidos(self,idFarmacia):
        return self.manager.MedicamentVendidos(int(idFarmacia))


#--------------------------------------------------Medico-------------------------------------------------------------

    def AddMedico(self,nomeMedico,morada, nif, cc, tel,especialidade):
        self.manager.AddMedico(nomeMedico,morada, nif, cc, tel,especialidade)

    def updateMedico(self,nomeMedico,morada, nif, cc, tel,especialidade):
        self.manager.UpdateMedico(nomeMedico,morada, nif, cc, tel,especialidade)

    def apagarMedico(self,nomeMedico):
        self.manager.DeleteMedico(nomeMedico)

    def SelectMedico(self,nomeMedico):
        return self.manager.GetMedico(nomeMedico)

    def listMedico(self):
        return self.manager.GetMedicos()

    def MedicosMaisReceitas(self):
        return self.manager.MedicosMaisReceitas()

    def MediaReceitaPorMedico(self,nomeMedico):
        return self.manager.MediaReceitaPorMedico(nomeMedico)



