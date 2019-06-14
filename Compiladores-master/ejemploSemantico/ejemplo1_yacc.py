#!/usr/bin/python
# -*- coding: utf-8 -*-

import ply.yacc as yacc
from ejemplo1_lex import tokens
from ejemplo1_ast import Nodo

precedence =(
             ('left', 'MAS','MENOS'),
             ('left', 'MULT','DIVISION')
            )

descartables = ('PARENIZQ', 'PARENDER')

def capturar(p):
  
  hijos = []
  
  for hijo in p[1:]:
    if hijo not in descartables:
      hijos.append(hijo)
  
  p[0] = Nodo(hijos)


def p_E(p):
  '''E : E MAS   E
       | E MENOS E
       | T'''
  capturar(p)
  
def p_T(p):
  '''T : T MULT     F
       | T DIVISION F
       | F'''
  capturar(p)

def p_F(p):
  '''F : PARENIZQ E PARENDER
       | NUMERO'''
  capturar(p)
  

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


yacc.yacc('SLR')
codigoFuente='3*5+4-10'
print(yacc.parse(codigoFuente).valor)

