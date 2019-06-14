#!/usr/bin/python
# -*- coding: utf-8 -*-

from graphviz import GraphViz

#3 Entrega Christian Herrera 9860957

class Node(GraphViz): 
    def __init__(self, hijos, tipo):
      GraphViz.__init__(self, hijos, tipo)
    
    def imprimir(self, tab):
      print tab + "   "+ "|"
      print tab + "   "+ "+->"+ self.tipo
      for hijo in self.hijos:
        try:
          hijo.imprimir(tab+"   ")
        except:
          print tab +"   " + "   " + "|"
          print tab +"   " + "   " + "*->" + str(hijo)
