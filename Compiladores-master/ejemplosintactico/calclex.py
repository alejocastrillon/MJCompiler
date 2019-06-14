# -*- coding: cp1252 -*-
# -----------------------------------------------------------------------------
# calcyacc.py
#
# Analizador léxico de expresiones aritméticas 
# -----------------------------------------------------------------------------

# importa el primer módulo del ply
import ply.lex as lex

tokens = (
    'NUMERO',
    'MAS','MENOS','MULT','DIVISION','IGUAL',
    'PARENIZQ','PARENDER', 'IDENT'
    )

# Tokens

t_MAS    = r'\+'
t_MENOS   = r'-'
t_MULT   = r'\*'
t_DIVISION  = r'/'
t_IGUAL  = r'='
t_PARENIZQ  = r'\('
t_PARENDER  = r'\)'
t_IDENT  = r'[a-z_][a-zA-Z0-9]*'

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

analizador=lex.lex()


