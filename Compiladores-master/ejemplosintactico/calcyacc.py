# -*- coding: cp1252 -*-
# Análisis sintáctico
# importa el primer módulo del ply

import ply.yacc as yacc

from calclex import tokens

def p_statement_assign(p):
    'statement : IDENT IGUAL expression'
    print("reduce statement : IDENT IGUAL expression")

def p_statement_expr(p):
    'statement : expression'
    print( 'statement : expression')

def p_expression_binop(p):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  
                  | expression MULT expression
                  
                  | expression DIVISION expression'''
    print('reduce statement : expression operador expression')

def p_expression_group(p):
    'expression : PARENIZQ expression PARENDER'
    print('reduce expression : PARENIZQ expression PARENDER')

def p_expression_number(p):
    'expression : NUMERO'
    print( 'reduce expression : NUMERO')
    

def p_expression_name(p):
    'expression : IDENT'
    print('reduce expression : IDENT')

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)


yacc.yacc('SLR')
codigoFuente='3+5+4-10'
yacc.parse(codigoFuente)

