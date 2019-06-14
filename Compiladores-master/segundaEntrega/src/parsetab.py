
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=leftoleftyleftcomparadornoIgualleft><menorIgualmayorIgualleft+-left*/%right!newuminusleft[]()noIgual comparador mayorIgual menorIgual o y id hexa numero cadenaCaracteres errorCadenaCaracteres comentarioUnilinea comentarioMultilinea errorComentarioMultilinea binario cientifico return string this void continue while else break int length boolean extends new false null true class ifPROGRAMA : CLASS_DECL_LIST\n              | epsilonCLASS_DECL_LIST : CLASS_DECL\n                     | CLASS_DECL CLASS_DECL_LISTCLASS_DECL : class id extends id '{' FIELD_OR_METHOD_DECL_LIST '}'\n                | class id extends id '{' '}'\n                | class id '{' FIELD_OR_METHOD_DECL_LIST '}'\n                | class id '{' '}' FIELD_OR_METHOD_DECL_LIST : FIELD_DECL \n                               | FIELD_DECL FIELD_OR_METHOD_DECL_LIST\n                               | METHOD_DECL\n                               | METHOD_DECL FIELD_OR_METHOD_DECL_LIST FIELD_DECL : TYPE id ';'\n                | TYPE id LIST_AUX_IDS ';' LIST_AUX_IDS : ',' id \n                  | ',' id LIST_AUX_IDSMETHOD_DECL : TYPE id '(' ')' BLOCK\n                 | TYPE id '(' FORMALS ')' BLOCK\n                 | void id '(' ')' BLOCK\n                 | void id '(' FORMALS ')' BLOCKFORMALS : TYPE id\n             | TYPE id ',' FORMALS TYPE : int \n          | boolean \n          | string \n          | id \n          | TYPE '[' ']' BLOCK : '{' '}'\n           | '{' VAR_DECL_STATEMENTS_LIST '}' VAR_DECL_STATEMENTS_LIST :  VAR_DECL\n                              |  VAR_DECL VAR_DECL_STATEMENTS_LIST\n                              |  STATEMENT\n                              |  STATEMENT VAR_DECL_STATEMENTS_LISTVAR_DECL : TYPE id LIST_IDS_EXPRESSIONS ';'\n              | TYPE id ';' \n              | TYPE id '=' EXPRESSION LIST_IDS_EXPRESSIONS ';'\n              | TYPE id '=' EXPRESSION ';' LIST_IDS_EXPRESSIONS : ',' id\n                          | ',' id '=' EXPRESSION\n                          | ',' id LIST_IDS_EXPRESSIONS\n                          | ',' id '=' EXPRESSION LIST_IDS_EXPRESSIONS STATEMENT : ASSIGN ';'\n               | CALL ';'\n               | return EXPRESSION ';'\n               | return ';'\n               | if '(' EXPRESSION ')' STATEMENT else STATEMENT\n               | if '(' EXPRESSION ')' STATEMENT\n               | while '(' EXPRESSION ')' STATEMENT\n               | break ';'\n               | continue ';'\n               | BLOCK ASSIGN : LOCATION '=' EXPRESSIONLOCATION : id\n              | EXPRESSION '.' id\n              | id '[' EXPRESSION ']' CALL : METHOD '(' ACTUALS ')'\n          | METHOD '(' ')' METHOD : id\n            | EXPRESSION '.' id ACTUALS : EXPRESSION\n             | EXPRESSION ',' ACTUALS EXPRESSION : LOCATION\n                | CALL\n                | this\n                | new id '(' ')'\n                | new TYPE '[' EXPRESSION ']'\n                | EXPRESSION '.' length\n                | BINARY_EXPRESSION\n                | '!' EXPRESSION\n                | '-' EXPRESSION %prec uminus\n                | LITERAL\n                | '(' EXPRESSION ')' BINARY_EXPRESSION : EXPRESSION '+' EXPRESSION\n                       | EXPRESSION '-' EXPRESSION\n                       | EXPRESSION '*' EXPRESSION\n                       | EXPRESSION '/' EXPRESSION\n                       | EXPRESSION '%' EXPRESSION\n                       | EXPRESSION y EXPRESSION\n                       | EXPRESSION o EXPRESSION\n                       | EXPRESSION '<' EXPRESSION\n                       | EXPRESSION menorIgual EXPRESSION\n                       | EXPRESSION '>' EXPRESSION\n                       | EXPRESSION mayorIgual EXPRESSION\n                       | EXPRESSION comparador EXPRESSION\n                       | EXPRESSION noIgual EXPRESSION LITERAL : numero\n             | binario\n             | hexa\n             | cientifico\n             | cadenaCaracteres\n             | true\n             | false\n             | null epsilon :"
    
_lr_action_items = {'false':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[51,-51,51,51,51,51,51,51,-28,51,51,51,-42,-45,-49,51,51,51,51,51,51,51,51,51,51,51,51,51,-29,51,51,-50,-43,51,-44,-35,51,51,51,51,-34,-47,-48,51,-37,51,-36,-46,]),'int':([9,12,14,21,30,32,35,43,44,45,48,55,63,67,71,82,83,84,85,97,98,101,117,120,121,131,153,163,165,168,172,175,176,],[16,16,16,16,16,16,-13,-14,16,-19,-17,-51,16,16,16,-28,16,-20,-18,-42,-45,-49,-29,-50,-43,-44,-35,-34,-47,-48,-37,-36,-46,]),'length':([110,126,],[139,139,]),'binario':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[52,-51,52,52,52,52,52,52,-28,52,52,52,-42,-45,-49,52,52,52,52,52,52,52,52,52,52,52,52,52,-29,52,52,-50,-43,52,-44,-35,52,52,52,52,-34,-47,-48,52,-37,52,-36,-46,]),'boolean':([9,12,14,21,30,32,35,43,44,45,48,55,63,67,71,82,83,84,85,97,98,101,117,120,121,131,153,163,165,168,172,175,176,],[17,17,17,17,17,17,-13,-14,17,-19,-17,-51,17,17,17,-28,17,-20,-18,-42,-45,-49,-29,-50,-43,-44,-35,-34,-47,-48,-37,-36,-46,]),'noIgual':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,104,-88,-63,-53,-62,-69,-63,104,-70,104,104,104,-72,104,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,104,-84,104,-81,-82,-57,104,104,-55,104,-65,-56,104,-66,104,]),'null':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[66,-51,66,66,66,66,66,66,-28,66,66,66,-42,-45,-49,66,66,66,66,66,66,66,66,66,66,66,66,66,-29,66,66,-50,-43,66,-44,-35,66,66,66,66,-34,-47,-48,66,-37,66,-36,-46,]),'id':([2,8,9,11,12,13,14,16,17,18,19,21,30,31,32,33,35,38,43,44,45,48,54,55,57,60,61,63,65,67,71,81,82,83,84,85,86,87,94,97,98,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,126,129,131,151,153,154,156,159,161,163,165,168,170,172,173,175,176,],[6,10,18,-25,18,23,18,-23,-24,-26,27,18,18,-27,18,42,-13,46,-14,54,-19,-17,-26,-51,88,88,88,96,88,54,54,122,-28,18,-20,-18,88,88,88,-42,-45,-49,88,88,88,88,88,88,88,140,88,88,88,88,88,88,-29,88,88,-50,-43,140,88,-44,162,-35,88,88,88,88,-34,-47,-48,88,-37,88,-36,-46,]),'if':([44,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[56,-51,56,56,-28,-42,-45,-49,-29,-50,-43,-44,-35,56,56,-34,-47,-48,-37,56,-36,-46,]),'!':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[57,-51,57,57,57,57,57,57,-28,57,57,57,-42,-45,-49,57,57,57,57,57,57,57,57,57,57,57,57,57,-29,57,57,-50,-43,57,-44,-35,57,57,57,57,-34,-47,-48,57,-37,57,-36,-46,]),'while':([44,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[78,-51,78,78,-28,-42,-45,-49,-29,-50,-43,-44,-35,78,78,-34,-47,-48,-37,78,-36,-46,]),'%':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,103,-88,-63,-53,-62,-69,-63,103,-70,103,103,103,-72,103,-77,103,103,103,-75,103,-76,-67,-54,103,103,103,103,103,103,-57,103,103,-55,103,-65,-56,103,-66,103,]),')':([30,32,39,41,46,51,52,53,58,59,66,69,70,72,73,77,88,89,90,91,92,93,118,123,125,127,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,155,158,160,166,167,],[37,40,47,49,-21,-92,-87,-89,-91,-68,-93,-71,-86,-90,-64,-88,-53,-62,-69,-63,127,-70,147,-22,156,-72,158,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,-60,160,161,-55,-65,-56,-66,-61,]),'(':([23,27,44,54,55,56,57,60,61,65,67,71,76,78,82,86,87,88,94,96,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,140,153,154,156,159,161,163,165,168,170,172,173,175,176,],[30,32,60,-58,-51,87,60,60,60,60,60,60,118,119,-28,60,60,-58,60,130,-42,-45,-49,60,60,60,60,60,60,60,60,60,60,60,60,60,-29,60,60,-50,-43,60,-44,-59,-35,60,60,60,60,-34,-47,-48,60,-37,60,-36,-46,]),'+':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,106,-88,-63,-53,-62,-69,-63,106,-70,106,106,106,-72,106,-77,106,106,-73,-75,-74,-76,-67,-54,106,106,106,106,106,106,-57,106,106,-55,106,-65,-56,106,-66,106,]),'*':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,107,-88,-63,-53,-62,-69,-63,107,-70,107,107,107,-72,107,-77,107,107,107,-75,107,-76,-67,-54,107,107,107,107,107,107,-57,107,107,-55,107,-65,-56,107,-66,107,]),'-':([44,51,52,53,54,55,57,58,59,60,61,62,65,66,67,69,70,71,72,73,74,77,80,82,86,87,88,89,90,91,92,93,94,97,98,99,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,124,125,127,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,153,154,155,156,157,158,159,160,161,163,164,165,166,168,170,172,173,174,175,176,],[61,-92,-87,-89,-53,-51,61,-91,-68,61,61,-62,61,-93,61,-71,-86,61,-90,-64,108,-88,-63,-28,61,61,-53,-62,-69,-63,108,-70,61,-42,-45,108,-49,61,61,61,61,61,61,61,61,61,61,61,61,61,-29,61,61,-50,-43,108,108,-72,108,61,-44,-77,108,108,-73,-75,-74,-76,-67,-54,108,108,108,108,108,108,-57,108,108,-35,61,-55,61,108,-65,61,-56,61,-34,108,-47,-66,-48,61,-37,61,108,-36,-46,]),',':([27,42,46,51,52,53,58,59,66,69,70,72,73,77,88,89,90,91,93,122,127,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,155,158,160,162,164,166,174,],[33,33,83,-92,-87,-89,-91,-68,-93,-71,-86,-90,-64,-88,-53,-62,-69,-63,-70,151,-72,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,159,-55,-65,-56,151,151,-66,151,]),'/':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,109,-88,-63,-53,-62,-69,-63,109,-70,109,109,109,-72,109,-77,109,109,109,-75,109,-76,-67,-54,109,109,109,109,109,109,-57,109,109,-55,109,-65,-56,109,-66,109,]),'cadenaCaracteres':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[72,-51,72,72,72,72,72,72,-28,72,72,72,-42,-45,-49,72,72,72,72,72,72,72,72,72,72,72,72,72,-29,72,72,-50,-43,72,-44,-35,72,72,72,72,-34,-47,-48,72,-37,72,-36,-46,]),'.':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,110,-88,-63,-53,-62,-69,-63,126,-70,126,126,126,-72,126,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,126,126,-55,126,-65,-56,126,-66,126,]),'extends':([6,],[8,]),'new':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[63,-51,63,63,63,63,63,63,-28,63,63,63,-42,-45,-49,63,63,63,63,63,63,63,63,63,63,63,63,63,-29,63,63,-50,-43,63,-44,-35,63,63,63,63,-34,-47,-48,63,-37,63,-36,-46,]),';':([27,34,42,50,51,52,53,58,59,64,65,66,68,69,70,72,73,77,79,80,88,89,90,91,93,99,122,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,152,155,158,160,162,164,166,169,171,174,177,],[35,43,-15,-16,-92,-87,-89,-91,-68,97,98,-93,101,-71,-86,-90,-64,-88,120,121,-53,-62,-69,-63,-70,131,153,-72,-52,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,163,-55,-65,-56,-38,172,-66,-40,175,-39,-41,]),'=':([54,62,88,122,140,155,162,],[-53,94,-53,154,-54,-55,170,]),'<':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,105,-88,-63,-53,-62,-69,-63,105,-70,105,105,105,-72,105,-77,105,-80,-73,-75,-74,-76,-67,-54,-83,105,105,105,-81,-82,-57,105,105,-55,105,-65,-56,105,-66,105,]),'$end':([0,1,3,4,5,7,20,25,29,36,],[-94,-2,-3,-1,0,-4,-8,-7,-6,-5,]),'return':([44,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[65,-51,65,65,-28,-42,-45,-49,-29,-50,-43,-44,-35,65,65,-34,-47,-48,-37,65,-36,-46,]),'string':([9,12,14,21,30,32,35,43,44,45,48,55,63,67,71,82,83,84,85,97,98,101,117,120,121,131,153,163,165,168,172,175,176,],[11,11,11,11,11,11,-13,-14,11,-19,-17,-51,11,11,11,-28,11,-20,-18,-42,-45,-49,-29,-50,-43,-44,-35,-34,-47,-48,-37,-36,-46,]),'void':([9,12,14,21,35,43,45,48,82,84,85,117,],[13,13,13,13,-13,-14,-19,-17,-28,-20,-18,-29,]),'numero':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[70,-51,70,70,70,70,70,70,-28,70,70,70,-42,-45,-49,70,70,70,70,70,70,70,70,70,70,70,70,70,-29,70,70,-50,-43,70,-44,-35,70,70,70,70,-34,-47,-48,70,-37,70,-36,-46,]),'else':([55,82,97,98,101,117,120,121,131,165,168,176,],[-51,-28,-42,-45,-49,-29,-50,-43,-44,-47,-48,-46,]),'break':([44,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[68,-51,68,68,-28,-42,-45,-49,-29,-50,-43,-44,-35,68,68,-34,-47,-48,-37,68,-36,-46,]),'mayorIgual':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,111,-88,-63,-53,-62,-69,-63,111,-70,111,111,111,-72,111,-77,111,-80,-73,-75,-74,-76,-67,-54,-83,111,111,111,-81,-82,-57,111,111,-55,111,-65,-56,111,-66,111,]),'menorIgual':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,115,-88,-63,-53,-62,-69,-63,115,-70,115,115,115,-72,115,-77,115,-80,-73,-75,-74,-76,-67,-54,-83,115,115,115,-81,-82,-57,115,115,-55,115,-65,-56,115,-66,115,]),'[':([11,16,17,18,19,31,38,54,81,88,95,96,],[-25,-23,-24,-26,26,-27,26,86,26,86,129,-26,]),']':([26,51,52,53,58,59,66,69,70,72,73,77,88,89,90,91,93,124,127,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,155,157,158,160,166,],[31,-92,-87,-89,-91,-68,-93,-71,-86,-90,-64,-88,-53,-62,-69,-63,-70,155,-72,31,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,-55,166,-65,-56,-66,]),'class':([0,3,20,25,29,36,],[2,2,-8,-7,-6,-5,]),'this':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[73,-51,73,73,73,73,73,73,-28,73,73,73,-42,-45,-49,73,73,73,73,73,73,73,73,73,73,73,73,73,-29,73,73,-50,-43,73,-44,-35,73,73,73,73,-34,-47,-48,73,-37,73,-36,-46,]),'o':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,112,-88,-63,-53,-62,-69,-63,112,-70,112,112,112,-72,112,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,-79,-84,-78,-81,-82,-57,112,112,-55,112,-65,-56,112,-66,112,]),'cientifico':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[53,-51,53,53,53,53,53,53,-28,53,53,53,-42,-45,-49,53,53,53,53,53,53,53,53,53,53,53,53,53,-29,53,53,-50,-43,53,-44,-35,53,53,53,53,-34,-47,-48,53,-37,53,-36,-46,]),'hexa':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[77,-51,77,77,77,77,77,77,-28,77,77,77,-42,-45,-49,77,77,77,77,77,77,77,77,77,77,77,77,77,-29,77,77,-50,-43,77,-44,-35,77,77,77,77,-34,-47,-48,77,-37,77,-36,-46,]),'true':([44,55,57,60,61,65,67,71,82,86,87,94,97,98,101,103,104,105,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,129,131,153,154,156,159,161,163,165,168,170,172,173,175,176,],[58,-51,58,58,58,58,58,58,-28,58,58,58,-42,-45,-49,58,58,58,58,58,58,58,58,58,58,58,58,58,-29,58,58,-50,-43,58,-44,-35,58,58,58,58,-34,-47,-48,58,-37,58,-36,-46,]),'continue':([44,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[79,-51,79,79,-28,-42,-45,-49,-29,-50,-43,-44,-35,79,79,-34,-47,-48,-37,79,-36,-46,]),'comparador':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,113,-88,-63,-53,-62,-69,-63,113,-70,113,113,113,-72,113,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,113,-84,113,-81,-82,-57,113,113,-55,113,-65,-56,113,-66,113,]),'y':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,114,-88,-63,-53,-62,-69,-63,114,-70,114,114,114,-72,114,-77,-85,-80,-73,-75,-74,-76,-67,-54,-83,114,-84,-78,-81,-82,-57,114,114,-55,114,-65,-56,114,-66,114,]),'{':([6,10,37,40,44,47,49,55,67,71,82,97,98,101,117,120,121,131,153,156,161,163,165,168,172,173,175,176,],[9,21,44,44,44,44,44,-51,44,44,-28,-42,-45,-49,-29,-50,-43,-44,-35,44,44,-34,-47,-48,-37,44,-36,-46,]),'>':([51,52,53,54,58,59,62,66,69,70,72,73,74,77,80,88,89,90,91,92,93,99,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,155,157,158,160,164,166,174,],[-92,-87,-89,-53,-91,-68,-62,-93,-71,-86,-90,-64,116,-88,-63,-53,-62,-69,-63,116,-70,116,116,116,-72,116,-77,116,-80,-73,-75,-74,-76,-67,-54,-83,116,116,116,-81,-82,-57,116,116,-55,116,-65,-56,116,-66,116,]),'}':([9,12,14,15,21,22,24,28,35,43,44,45,48,55,67,71,75,82,84,85,97,98,100,101,102,117,120,121,131,153,163,165,168,172,175,176,],[20,-9,-11,25,29,-10,-12,36,-13,-14,82,-19,-17,-51,-30,-32,117,-28,-20,-18,-42,-45,-31,-49,-33,-29,-50,-43,-44,-35,-34,-47,-48,-37,-36,-46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'FIELD_DECL':([9,12,14,21,],[12,12,12,12,]),'CLASS_DECL':([0,3,],[3,3,]),'CLASS_DECL_LIST':([0,3,],[4,7,]),'BLOCK':([37,40,44,47,49,67,71,156,161,173,],[45,48,55,84,85,55,55,55,55,55,]),'BINARY_EXPRESSION':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'LIST_AUX_IDS':([27,42,],[34,50,]),'LOCATION':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[62,89,89,89,89,62,62,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,62,89,62,89,62,]),'LIST_IDS_EXPRESSIONS':([122,162,164,174,],[152,169,171,177,]),'EXPRESSION':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[74,90,92,93,99,74,74,124,125,128,132,133,134,135,136,137,138,141,142,143,144,145,146,148,150,157,164,74,148,74,174,74,]),'METHOD':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'epsilon':([0,],[1,]),'VAR_DECL':([44,67,71,],[67,67,67,]),'FIELD_OR_METHOD_DECL_LIST':([9,12,14,21,],[15,22,24,28,]),'LITERAL':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'STATEMENT':([44,67,71,156,161,173,],[71,71,71,165,168,176,]),'FORMALS':([30,32,83,],[39,41,123,]),'METHOD_DECL':([9,12,14,21,],[14,14,14,14,]),'VAR_DECL_STATEMENTS_LIST':([44,67,71,],[75,100,102,]),'ASSIGN':([44,67,71,156,161,173,],[64,64,64,64,64,64,]),'ACTUALS':([118,159,],[149,167,]),'CALL':([44,57,60,61,65,67,71,86,87,94,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,129,154,156,159,161,170,173,],[80,91,91,91,91,80,80,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,80,91,80,91,80,]),'PROGRAMA':([0,],[5,]),'TYPE':([9,12,14,21,30,32,44,63,67,71,83,],[19,19,19,19,38,38,81,95,81,81,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> CLASS_DECL_LIST','PROGRAMA',1,'p_PROGRAMA','analizadorSintactico.py',40),
  ('PROGRAMA -> epsilon','PROGRAMA',1,'p_PROGRAMA','analizadorSintactico.py',41),
  ('CLASS_DECL_LIST -> CLASS_DECL','CLASS_DECL_LIST',1,'p_CLASS_DECL_LIST','analizadorSintactico.py',45),
  ('CLASS_DECL_LIST -> CLASS_DECL CLASS_DECL_LIST','CLASS_DECL_LIST',2,'p_CLASS_DECL_LIST','analizadorSintactico.py',46),
  ('CLASS_DECL -> class id extends id { FIELD_OR_METHOD_DECL_LIST }','CLASS_DECL',7,'p_CLASS_DECL','analizadorSintactico.py',50),
  ('CLASS_DECL -> class id extends id { }','CLASS_DECL',6,'p_CLASS_DECL','analizadorSintactico.py',51),
  ('CLASS_DECL -> class id { FIELD_OR_METHOD_DECL_LIST }','CLASS_DECL',5,'p_CLASS_DECL','analizadorSintactico.py',52),
  ('CLASS_DECL -> class id { }','CLASS_DECL',4,'p_CLASS_DECL','analizadorSintactico.py',53),
  ('FIELD_OR_METHOD_DECL_LIST -> FIELD_DECL','FIELD_OR_METHOD_DECL_LIST',1,'p_FIELD_OR_METHOD_DECL_LIST','analizadorSintactico.py',57),
  ('FIELD_OR_METHOD_DECL_LIST -> FIELD_DECL FIELD_OR_METHOD_DECL_LIST','FIELD_OR_METHOD_DECL_LIST',2,'p_FIELD_OR_METHOD_DECL_LIST','analizadorSintactico.py',58),
  ('FIELD_OR_METHOD_DECL_LIST -> METHOD_DECL','FIELD_OR_METHOD_DECL_LIST',1,'p_FIELD_OR_METHOD_DECL_LIST','analizadorSintactico.py',59),
  ('FIELD_OR_METHOD_DECL_LIST -> METHOD_DECL FIELD_OR_METHOD_DECL_LIST','FIELD_OR_METHOD_DECL_LIST',2,'p_FIELD_OR_METHOD_DECL_LIST','analizadorSintactico.py',60),
  ('FIELD_DECL -> TYPE id ;','FIELD_DECL',3,'p_FIELD_DECL','analizadorSintactico.py',64),
  ('FIELD_DECL -> TYPE id LIST_AUX_IDS ;','FIELD_DECL',4,'p_FIELD_DECL','analizadorSintactico.py',65),
  ('LIST_AUX_IDS -> , id','LIST_AUX_IDS',2,'p_LIST_AUX_IDS','analizadorSintactico.py',69),
  ('LIST_AUX_IDS -> , id LIST_AUX_IDS','LIST_AUX_IDS',3,'p_LIST_AUX_IDS','analizadorSintactico.py',70),
  ('METHOD_DECL -> TYPE id ( ) BLOCK','METHOD_DECL',5,'p_METHOD_DECL','analizadorSintactico.py',74),
  ('METHOD_DECL -> TYPE id ( FORMALS ) BLOCK','METHOD_DECL',6,'p_METHOD_DECL','analizadorSintactico.py',75),
  ('METHOD_DECL -> void id ( ) BLOCK','METHOD_DECL',5,'p_METHOD_DECL','analizadorSintactico.py',76),
  ('METHOD_DECL -> void id ( FORMALS ) BLOCK','METHOD_DECL',6,'p_METHOD_DECL','analizadorSintactico.py',77),
  ('FORMALS -> TYPE id','FORMALS',2,'p_FORMALS','analizadorSintactico.py',81),
  ('FORMALS -> TYPE id , FORMALS','FORMALS',4,'p_FORMALS','analizadorSintactico.py',82),
  ('TYPE -> int','TYPE',1,'p_TYPE','analizadorSintactico.py',86),
  ('TYPE -> boolean','TYPE',1,'p_TYPE','analizadorSintactico.py',87),
  ('TYPE -> string','TYPE',1,'p_TYPE','analizadorSintactico.py',88),
  ('TYPE -> id','TYPE',1,'p_TYPE','analizadorSintactico.py',89),
  ('TYPE -> TYPE [ ]','TYPE',3,'p_TYPE','analizadorSintactico.py',90),
  ('BLOCK -> { }','BLOCK',2,'p_BLOCK','analizadorSintactico.py',94),
  ('BLOCK -> { VAR_DECL_STATEMENTS_LIST }','BLOCK',3,'p_BLOCK','analizadorSintactico.py',95),
  ('VAR_DECL_STATEMENTS_LIST -> VAR_DECL','VAR_DECL_STATEMENTS_LIST',1,'p_VAR_DECL_STATEMENTS_LIST','analizadorSintactico.py',99),
  ('VAR_DECL_STATEMENTS_LIST -> VAR_DECL VAR_DECL_STATEMENTS_LIST','VAR_DECL_STATEMENTS_LIST',2,'p_VAR_DECL_STATEMENTS_LIST','analizadorSintactico.py',100),
  ('VAR_DECL_STATEMENTS_LIST -> STATEMENT','VAR_DECL_STATEMENTS_LIST',1,'p_VAR_DECL_STATEMENTS_LIST','analizadorSintactico.py',101),
  ('VAR_DECL_STATEMENTS_LIST -> STATEMENT VAR_DECL_STATEMENTS_LIST','VAR_DECL_STATEMENTS_LIST',2,'p_VAR_DECL_STATEMENTS_LIST','analizadorSintactico.py',102),
  ('VAR_DECL -> TYPE id LIST_IDS_EXPRESSIONS ;','VAR_DECL',4,'p_VAR_DECL','analizadorSintactico.py',107),
  ('VAR_DECL -> TYPE id ;','VAR_DECL',3,'p_VAR_DECL','analizadorSintactico.py',108),
  ('VAR_DECL -> TYPE id = EXPRESSION LIST_IDS_EXPRESSIONS ;','VAR_DECL',6,'p_VAR_DECL','analizadorSintactico.py',109),
  ('VAR_DECL -> TYPE id = EXPRESSION ;','VAR_DECL',5,'p_VAR_DECL','analizadorSintactico.py',110),
  ('LIST_IDS_EXPRESSIONS -> , id','LIST_IDS_EXPRESSIONS',2,'p_LIST_IDS_EXPRESSIONS','analizadorSintactico.py',114),
  ('LIST_IDS_EXPRESSIONS -> , id = EXPRESSION','LIST_IDS_EXPRESSIONS',4,'p_LIST_IDS_EXPRESSIONS','analizadorSintactico.py',115),
  ('LIST_IDS_EXPRESSIONS -> , id LIST_IDS_EXPRESSIONS','LIST_IDS_EXPRESSIONS',3,'p_LIST_IDS_EXPRESSIONS','analizadorSintactico.py',116),
  ('LIST_IDS_EXPRESSIONS -> , id = EXPRESSION LIST_IDS_EXPRESSIONS','LIST_IDS_EXPRESSIONS',5,'p_LIST_IDS_EXPRESSIONS','analizadorSintactico.py',117),
  ('STATEMENT -> ASSIGN ;','STATEMENT',2,'p_STATEMENT','analizadorSintactico.py',122),
  ('STATEMENT -> CALL ;','STATEMENT',2,'p_STATEMENT','analizadorSintactico.py',123),
  ('STATEMENT -> return EXPRESSION ;','STATEMENT',3,'p_STATEMENT','analizadorSintactico.py',124),
  ('STATEMENT -> return ;','STATEMENT',2,'p_STATEMENT','analizadorSintactico.py',125),
  ('STATEMENT -> if ( EXPRESSION ) STATEMENT else STATEMENT','STATEMENT',7,'p_STATEMENT','analizadorSintactico.py',126),
  ('STATEMENT -> if ( EXPRESSION ) STATEMENT','STATEMENT',5,'p_STATEMENT','analizadorSintactico.py',127),
  ('STATEMENT -> while ( EXPRESSION ) STATEMENT','STATEMENT',5,'p_STATEMENT','analizadorSintactico.py',128),
  ('STATEMENT -> break ;','STATEMENT',2,'p_STATEMENT','analizadorSintactico.py',129),
  ('STATEMENT -> continue ;','STATEMENT',2,'p_STATEMENT','analizadorSintactico.py',130),
  ('STATEMENT -> BLOCK','STATEMENT',1,'p_STATEMENT','analizadorSintactico.py',131),
  ('ASSIGN -> LOCATION = EXPRESSION','ASSIGN',3,'p_ASSIGN','analizadorSintactico.py',135),
  ('LOCATION -> id','LOCATION',1,'p_LOCATION','analizadorSintactico.py',139),
  ('LOCATION -> EXPRESSION . id','LOCATION',3,'p_LOCATION','analizadorSintactico.py',140),
  ('LOCATION -> id [ EXPRESSION ]','LOCATION',4,'p_LOCATION','analizadorSintactico.py',141),
  ('CALL -> METHOD ( ACTUALS )','CALL',4,'p_CALL','analizadorSintactico.py',145),
  ('CALL -> METHOD ( )','CALL',3,'p_CALL','analizadorSintactico.py',146),
  ('METHOD -> id','METHOD',1,'p_METHOD','analizadorSintactico.py',150),
  ('METHOD -> EXPRESSION . id','METHOD',3,'p_METHOD','analizadorSintactico.py',151),
  ('ACTUALS -> EXPRESSION','ACTUALS',1,'p_ACTUALS','analizadorSintactico.py',155),
  ('ACTUALS -> EXPRESSION , ACTUALS','ACTUALS',3,'p_ACTUALS','analizadorSintactico.py',156),
  ('EXPRESSION -> LOCATION','EXPRESSION',1,'p_EXPRESSION','analizadorSintactico.py',160),
  ('EXPRESSION -> CALL','EXPRESSION',1,'p_EXPRESSION','analizadorSintactico.py',161),
  ('EXPRESSION -> this','EXPRESSION',1,'p_EXPRESSION','analizadorSintactico.py',162),
  ('EXPRESSION -> new id ( )','EXPRESSION',4,'p_EXPRESSION','analizadorSintactico.py',163),
  ('EXPRESSION -> new TYPE [ EXPRESSION ]','EXPRESSION',5,'p_EXPRESSION','analizadorSintactico.py',164),
  ('EXPRESSION -> EXPRESSION . length','EXPRESSION',3,'p_EXPRESSION','analizadorSintactico.py',165),
  ('EXPRESSION -> BINARY_EXPRESSION','EXPRESSION',1,'p_EXPRESSION','analizadorSintactico.py',166),
  ('EXPRESSION -> ! EXPRESSION','EXPRESSION',2,'p_EXPRESSION','analizadorSintactico.py',167),
  ('EXPRESSION -> - EXPRESSION','EXPRESSION',2,'p_EXPRESSION','analizadorSintactico.py',168),
  ('EXPRESSION -> LITERAL','EXPRESSION',1,'p_EXPRESSION','analizadorSintactico.py',169),
  ('EXPRESSION -> ( EXPRESSION )','EXPRESSION',3,'p_EXPRESSION','analizadorSintactico.py',170),
  ('BINARY_EXPRESSION -> EXPRESSION + EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',174),
  ('BINARY_EXPRESSION -> EXPRESSION - EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',175),
  ('BINARY_EXPRESSION -> EXPRESSION * EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',176),
  ('BINARY_EXPRESSION -> EXPRESSION / EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',177),
  ('BINARY_EXPRESSION -> EXPRESSION % EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',178),
  ('BINARY_EXPRESSION -> EXPRESSION y EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',179),
  ('BINARY_EXPRESSION -> EXPRESSION o EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',180),
  ('BINARY_EXPRESSION -> EXPRESSION < EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',181),
  ('BINARY_EXPRESSION -> EXPRESSION menorIgual EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',182),
  ('BINARY_EXPRESSION -> EXPRESSION > EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',183),
  ('BINARY_EXPRESSION -> EXPRESSION mayorIgual EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',184),
  ('BINARY_EXPRESSION -> EXPRESSION comparador EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',185),
  ('BINARY_EXPRESSION -> EXPRESSION noIgual EXPRESSION','BINARY_EXPRESSION',3,'p_BINARY','analizadorSintactico.py',186),
  ('LITERAL -> numero','LITERAL',1,'p_LITERAL','analizadorSintactico.py',190),
  ('LITERAL -> binario','LITERAL',1,'p_LITERAL','analizadorSintactico.py',191),
  ('LITERAL -> hexa','LITERAL',1,'p_LITERAL','analizadorSintactico.py',192),
  ('LITERAL -> cientifico','LITERAL',1,'p_LITERAL','analizadorSintactico.py',193),
  ('LITERAL -> cadenaCaracteres','LITERAL',1,'p_LITERAL','analizadorSintactico.py',194),
  ('LITERAL -> true','LITERAL',1,'p_LITERAL','analizadorSintactico.py',195),
  ('LITERAL -> false','LITERAL',1,'p_LITERAL','analizadorSintactico.py',196),
  ('LITERAL -> null','LITERAL',1,'p_LITERAL','analizadorSintactico.py',197),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','analizadorSintactico.py',201),
]
