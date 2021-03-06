#!/usr/bin/python
# -*- coding: utf-8 -*-
import ply.lex as lex
import ply.yacc as yacc
from analizadorLexico import tokens
from ast import *

#ENTREGA 2 ANALIZADOR SINTACTICO
#CHRISTIAN HERRERA     9860957


literalesAgrupacion = [',','[',']','{','}','(',')',';','.']


def capturar(p, tipo):
  hijos = []
  
  for hijo in p[1:]:
    if hijo not in literalesAgrupacion:
      hijos.append(hijo)
  p[0] = Node(hijos, tipo)


precedence =(
             ('right', '='),
             ('left', 'o'),
             ('left', 'y'),
             ('left', 'comparador', 'noIgual'),
             ('left', '>','<','menorIgual','mayorIgual'),
             ('left', '+','-'),
             ('left', '*','/','%'),
             ('right', '!','new','uminus'),
             ('left', '[',']','(',')')
            )

#1. Reglas de la gramatica
def p_PROGRAMA(p):
  '''PROGRAMA : CLASS_DECL_LIST
              | epsilon'''
  capturar(p, "PROGRAMA")

def p_CLASS_DECL_LIST(p):
  '''CLASS_DECL_LIST : CLASS_DECL
                     | CLASS_DECL CLASS_DECL_LIST'''
  capturar(p, "LISTA DECLARACION DE CLASES")

def p_CLASS_DECL(p):
  '''CLASS_DECL : class id extends id '{' FIELD_OR_METHOD_DECL_LIST '}'
                | class id extends id '{' '}'
                | class id '{' FIELD_OR_METHOD_DECL_LIST '}'
                | class id '{' '}' '''
  capturar(p, "DECLARACION DE CLASES")
  
def p_FIELD_OR_METHOD_DECL_LIST(p):
  '''FIELD_OR_METHOD_DECL_LIST : FIELD_DECL 
                               | FIELD_DECL FIELD_OR_METHOD_DECL_LIST
                               | METHOD_DECL
                               | METHOD_DECL FIELD_OR_METHOD_DECL_LIST '''
  capturar(p, "LISTA DECLARACION DE CAMPOS Y/O METODOS")
                    
def p_FIELD_DECL(p):
  '''FIELD_DECL : TYPE id ';'
                | TYPE id LIST_AUX_IDS ';' '''
  capturar(p, "DECLARACION DE CAMPO")
  
def p_LIST_AUX_IDS(p):
  '''LIST_AUX_IDS : ',' id 
                  | ',' id LIST_AUX_IDS'''
  capturar(p, "LISTA AUXILIAR DE IDS")

def p_METHOD_DECL(p):
  '''METHOD_DECL : TYPE id '(' ')' BLOCK
                 | TYPE id '(' FORMALS ')' BLOCK
                 | void id '(' ')' BLOCK
                 | void id '(' FORMALS ')' BLOCK'''
  capturar(p, "DECLARACION DE METODO")
  
def p_FORMALS(p):
  '''FORMALS : TYPE id
             | TYPE id ',' FORMALS '''
  capturar(p, "FORMALS")
                       
def p_TYPE(p):
  '''TYPE : int 
          | boolean 
          | string 
          | id 
          | TYPE '[' ']' '''
  capturar(p, "TIPO")

def p_BLOCK(p):
  '''BLOCK : '{' VAR_DECL_LIST STATEMENTS_LIST '}'
           | '{' VAR_DECL_LIST '}'
           | '{' STATEMENTS_LIST '}'
           | '{' '}' '''
  capturar(p, "BLOQUE")
  

def p_VAR_DECL_LIST(p):
  '''VAR_DECL_LIST : VAR_DECL
                   | VAR_DECL VAR_DECL_LIST '''
  capturar(p, "LISTA DECLARACION DE VARIABLES")

def p_VAR_DECL(p):
  '''VAR_DECL : TYPE id LIST_IDS_EXPRESSIONS ';'
              | TYPE id ';' 
              | TYPE id '=' EXPRESSION LIST_IDS_EXPRESSIONS ';'
              | TYPE id '=' EXPRESSION ';' '''
  capturar(p, "DECLARACION DE VARIABLE")

def p_LIST_IDS_EXPRESSIONS(p):
  '''LIST_IDS_EXPRESSIONS : ',' id
                          | ',' id '=' EXPRESSION
                          | ',' id LIST_IDS_EXPRESSIONS
                          | ',' id '=' EXPRESSION LIST_IDS_EXPRESSIONS '''
  capturar(p, "LISTA DE IDS Y EXPRESIONES")
                          
def p_STATEMENTS_LIST(p):                      
  '''STATEMENTS_LIST : STATEMENT
                     | STATEMENT STATEMENTS_LIST '''
  capturar(p, "LISTA DE ENUNCIADOS")


def p_STATEMENT(p):
  '''STATEMENT : ASSIGN ';' 
               | CALL ';'
               | return EXPRESSION ';'
               | return ';'
               | if '(' EXPRESSION ')' STATEMENT else STATEMENT
               | if '(' EXPRESSION ')' STATEMENT
               | while '(' EXPRESSION ')' STATEMENT
               | break ';'
               | continue ';'
               | BLOCK '''
  capturar(p, "ENUNCIADO")
  
def p_ASSIGN(p):
  '''ASSIGN : LOCATION '=' EXPRESSION '''
  capturar(p, "ASIGNACION")
  
def p_LOCATION(p):
  '''LOCATION : id
              | EXPRESSION '.' id
              | EXPRESSION '[' EXPRESSION ']' '''
  capturar(p, "LOCACION")
  
def p_CALL(p):
  '''CALL : METHOD '(' ACTUALS ')'
          | METHOD '(' ')' ''' 
  capturar(p, "LLAMADA")
  
def p_METHOD(p):
  '''METHOD : id
            | EXPRESSION '.' id '''
  capturar(p, "METODO")

def p_ACTUALS(p):
  '''ACTUALS : EXPRESSION
             | EXPRESSION ',' ACTUALS '''
  capturar(p, "ACTUALS")
  
def p_EXPRESSION(p):
  '''EXPRESSION : LOCATION
                | CALL
                | this
                | new id '(' ')'
                | new TYPE '[' EXPRESSION ']'
                | EXPRESSION '.' length
                | BINARY_EXPRESSION
                | '!' EXPRESSION
                | '-' EXPRESSION %prec uminus
                | LITERAL
                | '(' EXPRESSION ')' '''
  capturar(p, "EXPRESION")

def p_BINARY(p):
  '''BINARY_EXPRESSION : EXPRESSION '+' EXPRESSION
                       | EXPRESSION '-' EXPRESSION
                       | EXPRESSION '*' EXPRESSION
                       | EXPRESSION '/' EXPRESSION
                       | EXPRESSION '%' EXPRESSION
                       | EXPRESSION y EXPRESSION
                       | EXPRESSION o EXPRESSION
                       | EXPRESSION '<' EXPRESSION
                       | EXPRESSION menorIgual EXPRESSION
                       | EXPRESSION '>' EXPRESSION
                       | EXPRESSION mayorIgual EXPRESSION
                       | EXPRESSION comparador EXPRESSION
                       | EXPRESSION noIgual EXPRESSION '''
  capturar(p, "EXPRESION BINARIA")

def p_LITERAL(p):
  '''LITERAL : numero
             | binario
             | hexa
             | cientifico
             | cadenaCaracteres
             | true
             | false
             | null '''
  capturar(p, "LITERAL")

def p_epsilon(p):
  'epsilon :'
  pass
  

def p_error(p):
  print("Error de sintaxis en el token '"+ str(p.value) +"' que aparece en la "+
        "linea numero "+ str(p.lineno))


parser = yacc.yacc()
#codigoFuente = open('../../test/quickSortMiniJava.txt', 'r').read()
codigoFuente = open('../../test/codigoMiniJavaBien.txt', 'r').read()
parser.parse(codigoFuente).imprimir("")                 
