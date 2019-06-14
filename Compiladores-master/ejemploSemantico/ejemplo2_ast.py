#!/usr/bin/python
# -*- coding: utf-8 -*-

class Nodo():
  def __init__(self,hijos):
    self.hijos = hijos
        
  def setTipo(self, tipo):
    self.tipo = tipo
    
    for hijo in self.hijos:
      try:
        hijo.setTipo(tipo)
      except:
        pass
        
  def imprimirTipo(self):
    print(self.tipo)
    
    for hijo in self.hijos:
      try:
        hijo.imprimirTipo()
      except:
        pass
    
  
