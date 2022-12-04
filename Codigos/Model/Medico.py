#!/usr/bin/python
#-*- coding: utf-8 -*-

from Personal import Personal

class Medico(Personal):

    def __init__(self):
        self.Cedula = None
        self.Especialidad = None

    def setCedula(self, cedula):
        self.Cedula = cedula

    def getCedula(self):
        return self.Cedula

    def setEspecialidad(self, especialidad):
        self.Especialidad = especialidad

    def getEspecialidad(self, ):
        return self.Especialidad

    def atenderPaciente(self, ):
        print("Atendiendo paciente!!")

