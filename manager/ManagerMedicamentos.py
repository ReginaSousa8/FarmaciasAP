# -*- coding: utf-8 -*-
from model.Medicamento import *
from db.DataBase import *

class ManagerMedicamentos():

    def __init__(self,db):
        self.DB = db

    def Add(self, nomeMedicamento,dosagem):
        rec = Medicamento(nomeMedicamento,dosagem)
        self.DB.InsertMedicamento(rec)

    def Get(self, nomeMedicamento):
        listRec = []
        rec = self.DB.SelectMedicamento(nomeMedicamento)
        if rec == None:
            raise Exception("Not found")
        listRec.append(rec)
        return self.CreateInfoMedicamento(listRec)

    def Update(self, nomeMedicamento, dosagem):
        rec = Medicamento(nomeMedicamento, dosagem)
        self.DB.UpdateMedico(rec)


    def GetAll(self):
        listRec= self.DB.SelectAllMedicamentos()
        return self.CreateInfoMedicamento(listRec)

    def Delete(self, nomeMedicamento):
        return self.DB.DeleteMedicamentos(nomeMedicamento)


    def CreateInfoMedicamento(self,listRec):
        content = []
        for val in listRec:
                info = {}
                info["Nome"] = val.nome
                info["Dosagem"] = val.dosagem
                content.append(info)
        return content
