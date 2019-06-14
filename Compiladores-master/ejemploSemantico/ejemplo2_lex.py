#!/usr/bin/python
# -*- coding: utf-8 -*-

# importa el primer módulo del ply
import ply.lex as lex

literals = (',')
tokens = ( 'int', 'float', 'id')

# Tokens

def t_int(t):
  r'int'
  return t

def t_float(t):
  r'float'
  return t

def t_id(t):
    r'\w+'
    return t

# Caracteres que se ignoran
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("No se reconoce el caracter '%s'" % t.value[0])
    t.lexer.skip(1)
    
# construye el analizador
analizador_lexico=lex.lex()

