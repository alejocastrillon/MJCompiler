# -*- coding: cp1252 -*-
import ply.lex as lex
CONST_SPECIAL_CHARACTERS = u'\xf1\xe1\xe9\xed\xf3\xfa\xc1\xc9\xcd\xd3\xda\xd1'

reserved = {
    'boolean':'BOOLEAN',
    'break' : 'BREAK',
    'class' : 'CLASS',
    'continue' : 'CONTINUE',
    'else' : 'ELSE',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'if' : 'IF',
    'int' : 'INT',
    'length' : 'LENGTH',
    'new' : 'NEW',
    'null' : 'NULL',
    'return' : 'RETURN',
    'string' : 'STRING',
    'this' : 'THIS',
    'true' : 'TRUE',
    'void' : 'VOID',
    'while' : 'WHILE'
}


tokens = ['AND',
          'ASSIGNMENT',
          'BINARY',
          'COMMA',
          'LINECOMMENT',
          'MULTILINECOMMENT',
          'RIGHTSQRBRACKET',
          'LEFTSQRBRACKET',
          'DIVISION',
          'NOTEQUAL',
          'CONCAT',
          'EQUAL',
          'NOT',
          'HEXADEC',
          'IDEN',
          'RIGHTBRACE',
          'LEFTBRACE',
          'GREATEREQUAL',
          'GREATER',
          'LESSEQUAL',
          'LESS',
          'SUBSTRACTION',
          'UMINUS',
          'MULTIPLICATION',
          'NUMBER',
          'CIENTIFIC',
          'FLOAT',
          'OR',
          'RIGHTPARENT',
          'LEFTPARENT',
          'MODULO',
          'DOT',
          'SEMICOLON',
          'ADDITION'
]

tokens += reserved.values()

t_AND = r'(\&\&|AND)'
t_ASSIGNMENT = r'='
t_COMMA = r','
t_LEFTSQRBRACKET = r'\['
t_RIGHTSQRBRACKET = r'\]'
t_DIVISION = r'\/'
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_NOT = r'!'
t_LEFTBRACE  = r'\{'
t_RIGHTBRACE = r'\}'
t_GREATEREQUAL = r'>='
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_LESS = r'<'
t_SUBSTRACTION = r'\-'
t_UMINUS = r'\-'
t_CONCAT = r'\+'
t_MULTIPLICATION = r'\*'
t_OR = r'(\|\|)|(OR)'
t_LEFTPARENT = r'\('
t_RIGHTPARENT = r'\)'
t_MODULO = r'%'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_ADDITION = '\+'

def t_FLOAT(t):
    r'(-)?(\d+\.\d+)'
    return t
    
def t_CIENTIFIC(t):
    r'[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(\s)?[eE](?:[+\-]?\d+)?'
    return t

def t_BINARY(t):
    r'b\'[01]+\''
    t.value  = t.value[2:]
    t.value = t.value[:-1]
    try:
        t.value  = int(t.value,2)
    except:
        print("ERROR CONVERSION NUMERO %d", t.value)
        t.value = 0
    return t

def t_HEXADEC(t):
    r'0[Xx][0-9a-fA-F]+'
    try:
        t.value  = int(t.value,16)
    except:
        print("ERROR CONVERSION NUMERO %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"( ([ -~]|(\\\"))+ )\"'
    return t

def t_ignore_LINECOMMENT(t):
    r'//(.)*(\n)?'

def t_ignore_MULTILINECOMMENT(t):
    r'(/\*)(.|\n|\r)*(\*\/)'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_IDEN(t):
    r'[_a-zA-Z_]([a-zA-Z_0-9]*[a-zA-Z])?'
    t.value = accentReplace(t.value)
    t.type = reserved.get(t.value,'IDEN')
    if len(t.value)>20:
        t.value = t.value[:20]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    line = t.lexer.lineno
    print("Caracter %s no reconocido en la linea %d" % (t.value[0], line))
    t.lexer.skip(1)

## Helper Functions ##
def accentReplace(word):
    identifier = ''
    for i in word:
        index = word.index(i)
        if i in CONST_SPECIAL_CHARACTERS:
            identifier += '_'
        else:
            identifier += i
    return identifier

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
//
class Test {
int partition(int [] a, int low, int high) {
int pivot = a[low];
int i = low;
int j = high;
int tmp;
while (true) {
while (a[i] < pivot) i = i+1;
while (a[j] > pivot) j = j-1;
if (i >= j) break;
tmp = a[i];
a[i] = a[j];
a[j] = tmp;
i = i + 1;
j = j - 1;
}
return j;
}
void quicksort(int [] a, int low, int high) {
if (low < high) {
int mid = partition(a, low, high);
quicksort(a, low, mid);
quicksort(a, mid+1, high);
}
}
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 print(tok)
