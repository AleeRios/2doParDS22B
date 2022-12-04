#!/usr/bin/python
#-*- coding: utf-8 -*-

class Personal:

    def __init__(self):
        self.Nombre = None
        self.Puesto = None

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getNombre(self):
        return self.Nombre

    def setPuesto(self, puesto):
        self.Puesto = puesto

    def getPuesto(self):
        return self.Puesto

