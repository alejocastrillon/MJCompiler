class Nodo:
    pass

class ExpOp(Nodo):
    def __init__(self, op1, op, op2):
        self.op1=op1
        self.op=op
        self.op2=op2
                    
        
class ExpGrupo(Nodo):
    def __init__(self, exp):
        self.exp=exp
    
        
   

class ExpNumero(Nodo):
    def __init__(self, valor):
        self.valor=valor
   
        
        
        
    
    
