#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, hijos, tipo):
      self.hijos = hijos
      self.tipo  = tipo
    
    def imprimir(self, tab):
      print tab + "   "+ "|"
      print tab + "   "+ "+->"+ self.tipo
      for hijo in self.hijos:
        try:
          hijo.imprimir(tab+"   ")
        except:
          print tab +"   " + "   " + "|"
          print tab +"   " + "   " + "*->" + str(hijo)
