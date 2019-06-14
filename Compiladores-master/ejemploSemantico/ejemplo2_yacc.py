#!/usr/bin/python
# -*- coding: utf-8 -*-

import ply.yacc as yacc
from ejemplo2_lex import tokens
from ejemplo2_ast import Nodo



descartables = (',',',')

def capturar(p):
  
  hijos = []
  
  for hijo in p[1:]:
    if hijo not in descartables:
      hijos.append(hijo)
  
  p[0] = Nodo(hijos)


def p_DECL(p):
  '''DECL : TYPE VAR_LIST'''
  capturar(p)
  
def p_TYPE(p):
  '''TYPE : int
          | float'''
  capturar(p)

def p_VAR_LIST(p):
  '''VAR_LIST : id ',' VAR_LIST
              | id'''
  capturar(p)
  

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


yacc.yacc('SLR')
codigoFuente='float x,y,z'
nodoRaiz = yacc.parse(codigoFuente)
tipo = nodoRaiz.hijos[0].hijos[0]
nodoRaiz.setTipo(tipo)
nodoRaiz.imprimirTipo()
