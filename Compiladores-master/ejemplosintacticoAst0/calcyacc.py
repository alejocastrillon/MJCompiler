# -*- coding: cp1252 -*-
# Análisis sintáctico
# importa el primer módulo del ply

import ply.lex as lex
import ply.yacc as yacc
from calclex import tokens
from astCalc import *

precedence =(('left', 'MAS', 'MENOS'),
             ('left', 'MULT', 'DIVISION'))

def p_expression_binop(p):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  | expression MULT expression
                  | expression DIVISION expression'''
    p[0]=ExpOp(p[1], p[2], p[3])

def p_expression_group(p):
    'expression : PARENIZQ expression PARENDER'
    p[0]=ExpGrupo(p[2])

def p_expression_number(p):
    'expression : NUMERO'
    p[0]=ExpNumero(p[1])
    
def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

yacc.yacc()
codigoFuente='(5+4)*3'
nodoRaiz=yacc.parse(codigoFuente)


