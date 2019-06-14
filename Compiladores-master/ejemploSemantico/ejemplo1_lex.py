#!/usr/bin/python
# -*- coding: utf-8 -*-

# importa el primer m�dulo del ply
import ply.lex as lex

tokens = ( 'NUMERO', 'MAS', 'MENOS', 'MULT','DIVISION', 
           'PARENIZQ','PARENDER')

# Tokens

t_MAS       = r'\+'
t_MENOS     = r'-'
t_MULT      = r'\*'
t_DIVISION  = r'/'
t_PARENIZQ  = r'\('
t_PARENDER  = r'\)'

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor no es correcto %d", t.value)
        t.value = 0
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


