#!/usr/bin/python
# -*- coding: utf-8 -*-
import ply.lex as lex

#ENTREGA 1 ANALIZADOR LEXICO
#JOHN FREDDY SALAMANCA 1088317765
#CHRISTIAN HERRERA     9860957

#1. Diccionario de palabras reservadas
                     #  keys       values
palabrasReservadas  = {'class'   :'class',
    	     	       		 'return'  :'return',
    	                 'this'    :'this',
					   					 'extends' :'extends',
					   					 'if'      :'if',
					   					 'new'     :'new',
					   					 'void'    :'void',
					   					 'else'    :'else',
					  					 'length'  :'length',
					   					 'int'     :'int',
					   					 'while'   :'while',
					   					 'true'    :'true',
					   					 'boolean' :'boolean',
					   					 'break'   :'break',
					   					 'false'   :'false',
					   					 'string'  :'string',
					   					 'continue':'continue',
					   					 'null'    :'null',
				     					}

#2. Lista de caracteres a reemplazar por "_"
listaCaracteresEspeciales = ['á','é','í','ó','ú','ñ','Á','É','Í','Ó','Ú','Ñ']


# Literales para usar tokens que solo tienen un lexema dentro del
# analizador sintactico (Ej: en vez de escribir una regla
# OPERACION = num mas num, se puede escribir mas simple
# OPERACION = num '+' num)
# Si voy a usar literales, no debo declarar esos literales como tokens
# Los literales solo se pueden usar para tokens de un caracter de largo
# Para todo lo demas, si toca declararlos como tokens
literals = [',','[',']','+','-','*','/','=','!','{','}','>','<','(',')',';','.','%']


#3. Definicion de tokens
tokens = [#'coma',
		      #'corcheteIzq',
		      #'corcheteDer',
		      #'mas',
		      #'menos',
		      #'mult',
	        #'division',
		      #'igual',
		      'noIgual',
		      'comparador',
	        #'no',
	        #'llaveIzq',
	        #'llaveDer',
	        #'mayor',
	        'mayorIgual',
	        #'menor',
	        'menorIgual',
	        'o',
	        'y',
	        #'parenIzq',
	        #'parenDer',
	        'id',
		      'hexa',
		      'numero',
		      'cadenaCaracteres',
		      'errorCadenaCaracteres',
		      #'puntoComa',
	        #'punto',	
		      #'modulo',
	        'comentarioUnilinea',
		      'comentarioMultilinea',
		      'errorComentarioMultilinea',
		      'binario',
		      'cientifico'
				#Anexo a la lista de tokens inicial los valores del diccionario de 
				#palabras reservadas
         ] + list(palabrasReservadas.values())

#4. Tokens como variables o expresiones regulares
#t_coma 					= r','
#t_corcheteIzq   = r'\['
#t_corcheteDer 	= r'\]'
#t_mas    				= r'\+'
#t_mult   				= r'\*'
#t_division  		= r'\/'
#t_igual  				= r'='
t_noIgual 			= r'!='
t_comparador		= r'=='
#t_no						= r'!'
#t_llaveIzq			= r'{'
#t_llaveDer			= r'}'
#t_mayor					= r'>'
t_mayorIgual		= r'>='
#t_menor					= r'<'
t_menorIgual		= r'=<'
t_o 						= r'\|\|'
t_y 						= r'&&'
#t_parenIzq  		= r'\('
#t_parenDer  		= r'\)'
#t_puntoComa 		= r';'
#t_punto 				= r'\.'
#t_modulo 				= r'%'


#5. Tokens como funciones 
t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_cadenaCaracteres(t):
	r'".*"'
	return t
   
def t_errorCadenaCaracteres(t):
	#Las comillas sin cerrar se evaluan hasta el fin de 
	#una linea (salto de linea) o cuando el error se encuentra en 
	#la ultima linea, se usa el caracter $ que representa End Of File	
	r'".+(\n|$)'
	print("\n*************************ERROR!!!!!***************************")	
	print("Comillas sin cerrar en la linea %d" %t.lineno)
	print("**************************************************************\n")
	#toca sumarle 1 al contador de lineas del lexer porque si \n esta
	#dentro de un token, no lo detecta en la funcion t_newline()	
	t.lexer.lineno += 1
	
def t_error(t):
	print("\n*************************ERROR!!!!!***************************")	
	print("No se reconoce el caracter '%s' de la linea %d" %(t.value[0],t.lineno))
	print("**************************************************************\n")
	t.lexer.skip(1)

def t_comentarioUnilinea(t):
	r'//.*\n'
	#toca sumarle 1 al contador de lineas del lexer porque si \n esta
	#dentro de un token, no lo detecta en la funcion t_newline()	
	t.lexer.lineno += 1

def t_comentarioMultilinea(t):
  #el ? que aparece en la expresion sirve para usar la expresion en 
	#modo lazy y no en greedy
	#En modo greedy tendria un problema si hay dos comentarios multilinea 
	#dentro del codigo
	#Buscar en google "ejemplos regex modo greedy" para mayor informacion
	r'/\*(.|\n)*?\*/'
	#toca sumar el numero de lineas al contador de lineas del lexer 
  #porque si \n esta dentro de un token, no lo detecta en la 
	#funcion t_newline()
	t.lexer.lineno += t.value.count("\n")

def t_errorComentarioMultilinea(t):
	r'/\*(.|\n)+$'
	print("\n*************************ERROR!!!!!***************************")	
	print("Comentario multilinea sin cerrar en la linea %d" %t.lineno)
	print("**************************************************************\n")

def t_binario(t):
	r'b’[01]+’'
	#aplico manipulacion de cadenas para extraer la parte de 0s y 1s 
	#que es la que me interesa convertir a formato decimal
	primeracomilla = t.value.find("’")
	#por alguna extraña razon el simbolo ’ ocupa 3 caracteres y no uno 
	ultimacomilla  = t.value.find("’",primeracomilla + 3)
	numerobinario  = t.value[primeracomilla + 3:ultimacomilla]
	print("el numero binario %s es %d en decimal " \
	%(numerobinario,int(numerobinario,2)))
	t.value = int(numerobinario,2)
	return t

def t_id(t):
	r'([a-zA-Z_]+[a-zA-ZáéíóúñÁÉÍÓÚÑ0-9_]*[a-zA-ZáéíóúñÁÉÍÓÚÑ_])|[a-zA-Z]'
  #primero busco si la cadena es reservada para cambiarle el tipo de TOKEN
  #si la palabra no es reservada t.type continua siendo 'id'
	t.type = palabrasReservadas.get(t.value,'id')
  #si la palabra es un id, procedo a buscar si tiene 
	#caracteres especiales que se deban reemplazar
	if t.type == "id":
		for caracterEspecial in listaCaracteresEspeciales:
			t.value = t.value.replace(caracterEspecial,'_')
	return t

def t_hexa(t):
	r'0[xx][0-9a-fa-f]+'
	print("el numero hexadecimal %s es %d en el sistema decimal" \
	      %(t.value,int(t.value,16)))        	
	t.value = int(t.value,16)
	return t

def t_cientifico(t):
	r'-?[0-9](\.\d+)?[ee]-?\d+'
	t.value=float(t.value)
	return t
	
def t_numero(t):
	r'(\d+)' 
	t.value = int(t.value)
	if t.value < -2147483648 or t.value > 2147483647:
		print("\n*************************ERROR!!!!!***************************")
		print("el numero %d que aparece en la linea %d no esta permitido" \
					%(t.value,t.lineno))
		print("**************************************************************\n")
	else: return t


#6. Creacion del analizador
analizador = lex.lex()
