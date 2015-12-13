grammar LatexGram;

atom
  : NUM | ZERO | ONE | VAR
  : '{' tex '}' ;

MUL : '*' | '\\times' | '\\cdot' ;
ADD : '+' ;
SUB : '-' ;
DIV : '/' ;


NUM : [0-9]+ ;
ZERO: 0;
ONE : 1;

WS : [ \t\r\n]+ -> skip ;

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
