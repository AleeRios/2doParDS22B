#!/usr/bin/python
#-*- coding: utf-8 -*-

class Paciente:

    def __init__(self):
        self.Nombre = None
        self.Edad = None
        self.Direccion = None

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setEdad(self, edad):
        self.Edad = edad

    def getEdad(self):
        return self.Edad

    def setDireccion(self, direccion):
        self.Direccion = direccion

    def getDireccion(self):
        return self.Direccion

