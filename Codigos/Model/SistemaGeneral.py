#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
from datetime import datetime
from Paciente import Paciente
from Medico import Medico

class SistemaGeneral:

    def __init__(self):
        self.Nombre = None
        self.Direccion = None

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def getDireccion(self):
        return self.Direccion

    def sacarCita(self):
        ini = datetime(2022, 12, 8)
        fin = datetime(2023, 1, 8)
        fecha = ini + (fin - ini) * random.random()
        print("Cita sacada con exito el dia: ", fecha)

    def consultaMedica(self):
        print("Espere su turno para pasar a consulta!!")

def main():
    sg = SistemaGeneral()
    pa = Paciente()
    med = Medico()

    pa.setNombre("Beckham Alejandro Rios Campusano")
    pa.setEdad(24)
    pa.setDireccion("Zumpango")

    med.setNombre("Uriel Sanchez Morales")
    med.setPuesto("Medico")
    med.setCedula(341298613)
    med.setEspecialidad("Medico Cirujano")

    print("Paciente: " + str(pa.getNombre()), "Edad: "+ str(pa.getEdad()), "Direccion: " + str(pa.getDireccion()), sep="\n")
    sg.sacarCita()
    print("Lo va atender: ")
    print("Medico: " + str(med.getNombre()),"Puesto: " + str(med.getPuesto()), "Cedula: " + str(med.getCedula()), "Especialidad: " + str(med.getEspecialidad()), sep="\n")
    med.atenderPaciente()

main()