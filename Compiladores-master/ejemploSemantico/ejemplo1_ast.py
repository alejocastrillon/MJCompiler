#!/usr/bin/python
# -*- coding: utf-8 -*-

class Nodo():
  def __init__(self,hijos):
    self.hijos = hijos
    self.valor = self.evaluar()
    
  def evaluar(self):
    #Si tiene un solo hijo
    if(len(self.hijos) == 1):
      try:
        return self.hijos[0].valor
      except:
        return self.hijos[0]
    
    #Si tiene varios hijos
    operador = self.hijos[1]    
    if(operador == '+'): valor = self.hijos[0].valor + self.hijos[2].valor
    if(operador == '-'): valor = self.hijos[0].valor - self.hijos[2].valor     
    if(operador == '*'): valor = self.hijos[0].valor * self.hijos[2].valor
    if(operador == '/'): valor = self.hijos[0].valor / self.hijos[2].valor
    
    return valor

