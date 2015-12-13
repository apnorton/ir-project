grammar LatexGram;

s : expr;

expr 
  : atom          # atomic
  | pack          # packed
  | expr MUL expr # Mul
  | pack pack     # iMul
  | expr '^' atom # pow
  | expr ADD expr # add
  | expr SUB expr # sub
  | expr DIV expr # div
  ;


pack
  : '(' expr ')'
  | '[' expr ']'
  ;

atom
  : NUM | ZERO | ONE | VAR
  | VAR atom
  | atom VAR
  | '{' expr '}' ;

MUL : '*' | '\\times' | '\\cdot' ;
ADD : '+' ;
SUB : '-' ;
DIV : '/' ;


NUM : [0-9]+ ;
ZERO: '0';
ONE : '1';


VAR 
  : [a-zA-Z]
  | '\\alpha'
  | '\\beta'
  | '\\delta'
  | '\\epsilon'
  | '\\zeta'
  | '\\eta'
  | '\\theta' 
  | '\\iota'
  | '\\kappa' 
  | '\\lambda'   
  | '\\mu'
  | '\\nu'  
  | '\\xi'  
  | '\\pi'  
  | '\\rho'  
  | '\\sigma'
  | '\\tau'
  | '\\upsilon'
  | '\\phi'
  | '\\chi'
  | '\\psi'
  | '\\omega'
  ;


WS : [ \t\r\n]+ -> skip ;
