
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\x0e\x109\xb81v\x04.\x08\xa5\xd3\xf5z}\xabb'

_lr_action_items = {'STRING':([8,11,17,22,],[10,10,-5,10,]),')':([20,],[21,]),'(':([18,],[20,]),'CLASS':([0,2,19,],[3,3,-4,]),';':([14,26,],[17,28,]),'INTEGER':([8,11,17,22,],[13,13,-5,13,]),'{':([7,21,],[8,22,]),'}':([16,23,25,27,28,],[19,25,-6,-7,-8,]),'ID':([3,8,9,10,11,12,13,15,17,22,24,],[7,12,14,-10,12,-11,-9,18,-5,12,26,]),'$end':([0,1,2,4,5,6,19,],[-12,-1,-12,0,-3,-2,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Body':([22,],[23,]),'DeclList':([0,2,],[1,6,]),'ClassDecl':([0,2,],[2,2,]),'FieldDecl':([8,22,],[11,24,]),'Program':([0,],[4,]),'MethDecl':([11,],[16,]),'Statement':([24,],[27,]),'Type':([8,11,22,],[9,15,9,]),'empty':([0,2,],[5,5,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('Program',1,'p_Program','./Micro.py',71),
  ('DeclList',2,'p_DeclList','./Micro.py',75),
  ('DeclList',1,'p_DeclList1','./Micro.py',79),
  ('ClassDecl',6,'p_ClassDecl','./Micro.py',83),
  ('FieldDecl',3,'p_FieldDecl','./Micro.py',87),
  ('MethDecl',7,'p_MethDecl','./Micro.py',91),
  ('Body',2,'p_Body','./Micro.py',95),
  ('Statement',2,'p_Statement','./Micro.py',99),
  ('Type',1,'p_Type','./Micro.py',103),
  ('Type',1,'p_Type','./Micro.py',104),
  ('Type',1,'p_Type','./Micro.py',105),
  ('empty',0,'p_empty','./Micro.py',110),
]
