#!/usr/bin/python
# -*- coding: cp1252 -*-
#Ver 6.10 AST Construction del manual de referencia

cont=0
def incrementarContador():
    global cont 
    cont += 1
    return "%d " % cont

class Node: 
    pass

class NullNode(Node):
    "Representa un nodo nulo, despues de una produccion vacia"
    def __init__(self, t):
        self.t=t
    
    def traducir(self):
       
        self.id =incrementarContador()
        self.txt = self.id + " [label= "+self.t+"]\n\t"
        return (self.id, self.txt)

class Program(Node):
    """Programa contiene una lista de declaraciones,
    cambiar para disminuir la profundidad del arbol"""
    def __init__(self, declList):
        self.declList = declList
        self.name="Program"
    
    def traducir(self):
       
        self.id = incrementarContador()
        (self.declList, self.dtxt) = self.declList.traducir()
        self.txt = self.dtxt
        self.txt += self.id + " [label= "+self.name+", shape=box]\n\t"
        self.txt += self.id + " -> " + self.declList + "\n\t"
        return "digraph G {\n"+self.txt+"\n}"
    
class DeclList(Node): 
    """ Lista las clases 
        Utilizar NodeList (para disminuir la profundidad del arbol 
    """
    def __init__(self, classDecl, declList):
        self.classDecl = classDecl
        self.declList = declList
        self.name="DeclList"
        
    def traducir(self):
        self.id = incrementarContador()
        (self.classDeclt, self.ctxt) = self.classDecl.traducir()
        (self.declListt, self.dtxt) = self.declList.traducir()
        self.txt = self.ctxt
        self.txt += self.dtxt
        
        self.txt += self.id + " [label= "+self.name+"]\n\t"
        self.txt += self.id + ' -> ' + self.classDeclt + '[color="0.515 0.762 0.762"] \n\t'
        self.txt += self.id + " -> " + self.declListt + "\n\t"
        
        return (self.id, self.txt)
    
class ClassDecl(Node):
    "Un nodo representando una declaracion de una clase."
    def __init__(self, name, fieldDecl, methDecl):
        self.name = name
        self.fieldDecl = fieldDecl
        self.methDecl = methDecl
        
    def traducir(self):
        self.id = incrementarContador()
        (self.fieldDecl, self.ftxt) = self.fieldDecl.traducir()
        (self.methDecl, self.mtxt) = self.methDecl.traducir()
        self.txt = self.ftxt
        self.txt += self.mtxt
        self.txt += self.id + " [label= "+self.name.name+", color=blue]\n\t"

        self.txt += self.id + " -> " + self.fieldDecl + "\n\t"
        self.txt += self.id + " -> " + self.methDecl + "\n\t"
        return (self.id, self.txt)


class FieldDecl(Node):
    "Nodo que representa la declaracion de atributos de la clase."
    def __init__(self, type, name ):
        self.type=type
        self.name=name
    def traducir(self):
        
        self.id = incrementarContador()
        (self.type, self.ttxt)=self.type.traducir()
        self.txt = self.ttxt
        self.txt += self.id + " [label= "+self.name+"]\n\t"
        
        self.txt += self.id + " -> " + self.type + "\n\t"
        #self.self.txt += self.id + " -> " + nodoname + "\n\t"
        return (self.id, self.txt)
   

class MethDecl(Node):
    "Nodo que representa la declaracion de metodo (sus declaraciones y cuerpo)."
    def __init__(self, type, name, body):
        self.type=type
        self.name=name
        self.body=body    
            
    def traducir(self):
        self.id = incrementarContador()

        (self.type, self.ttxt) =self.type.traducir()
        (self.body, self.btxt) =self.body.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.name+"]\n\t"
        
        self.txt += self.id + " -> " + self.type + "\n\t"
        self.txt += self.id + " -> " + self.body + "\n\t"
        return (self.id, self.txt)
        
    
class Statement(Node):
    """Nodo que representa un solo tipo de statement """
    def __init__(self, expr):
        self.expr = expr
        self.name="Statement"
    def traducir(self):
       
        self.id = incrementarContador()
        
        self.txt = self.id +" [label= "+self.name+"]\n\t"
        return (self.id, self.txt)

    


class Body(Node):
    "Nodo que representa el cuerpo de un metodo."
    def __init__(self, fieldDecl, statement):
        self.fieldDecl=fieldDecl
        self.statement=statement
        self.name="Body"
    
    def traducir(self):
        global txt
        self.id = incrementarContador()

        (self.statement, self.txt)=self.statement.traducir()
        
        self.txt += self.id +" [label= "+self.name+"]\n\t"

        self.txt += self.id + " -> " + self.statement + "\n\t"
        return (self.id, self.txt)
    
class Type(Node):
    def __init__(self, child=None):
        if child == None:
            child = NullNode()
        self.child = child

    def traducir(self):
        self.id = incrementarContador()
        
        self.txt = self.id +" [label= type]\n\t"
        return (self.id, self.txt)

class Id(Node):
    def __init__(self, name, lineno):
        self.name = name
        print self.name
        self.lineno = lineno
    def traducir(self):
        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.name+"]\n\t"
        return (self.id, self.txt)
