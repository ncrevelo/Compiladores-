grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' ID ')' '{' stat+ '}' 
    ;

stat
    : expr ';' 
    | ID '=' expr ';'
    ;

expr
    : expr '+' term  # AddExpr
    | term           # TermExpr
    ;

term
    : INT            # IntTerm
    | ID             # IdTerm
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z]+ ;
WS  : [ \t\r\n]+ -> skip ;
