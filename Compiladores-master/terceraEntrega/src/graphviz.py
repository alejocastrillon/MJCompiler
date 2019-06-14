#!/usr/bin/python
# -*- coding: utf-8 -*-

#3 Entrega Christian Herrera 9860957

class GraphViz():
  #-----------------------------------------------------------------------------
  def __init__(self, hijos, tipo):
      self.hijos = hijos
      self.tipo  = tipo
  
  #-----------------------------------------------------------------------------
  #funcion que me genera el cuerpo del codigo_DOT recursivamente
  def generarCodigoIntermedio(self, numeroId):
    
    #primero genero la informacion mia (Nodo padre)
    self.id    = numeroId
    codigo_DOT = str(self.id)+ " [label = \""+ self.tipo+\
                 "\", shape=\"polygon\", sides=\"4\"]\n"
    
    for hijo in self.hijos:
      #genero mis enlaces con mis hijos
      numeroId    = numeroId + 1
      codigo_DOT += str(self.id)+" -> "+str(numeroId)+"\n"
      
      try:
        #genero recursivamente la informacion de mis hijos no terminales
        (temp, numeroId)   = hijo.generarCodigoIntermedio(numeroId)
        codigo_DOT += temp
      except:
        #si tengo un hijo nodo hoja, simplemente genero su info manualmente
        codigo_DOT += str(numeroId)+" [label = \""+str(hijo)+\
                      "\", color =\"#f6d6ed\", style=\"filled\"]\n"
    
    #devuelvo el codigo que llevo construido al momento y tambien el ultimo
    #numeroID que genere para que mis hermanos sepan desde que numero deben
    #continuar sus numeroIDs
    return (codigo_DOT, numeroId)
  
  #-----------------------------------------------------------------------------
  #funcion que genera el codigo DOT, agrega el encabezado y el final y llama
  #a otra funcion que genere el cuerpo del codigo DOT recursivamente
  def generarCodigo_DOT(self):
    (codigo, i) = self.generarCodigoIntermedio(0)
    return "digraph G {\n"+codigo+"}"
