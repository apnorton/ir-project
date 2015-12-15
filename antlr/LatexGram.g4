grammar LatexGram;

s : expr;

expr 
  : atom          # atomic
  | pack          # packed
  | pack '^' pack # pow
  | BIG_OP expr   # bigOp
  | pack pack     # iMul
  | expr DIV expr # div
  | expr MUL expr # mul
  | expr SUB expr # sub
  | expr ADD expr # add
  | TRIG_OP pack  # trig
  ;

pack
  : atom          
  | '(' expr ')'  
  | '[' expr ']'  
  ;

atom
  : NUM             # atmNum
  | VAR             # atmVar
  | '{' expr '}'    # atmExpr
  ; 

MUL : '*' | '\\times' | '\\cdot' ;
ADD : '+' ;
SUB : '-' ;
DIV : '/' ;


NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;

/* Variable characters */
VAR 
  : [a-zA-Z]
  | '\\alpha'
  | '\\beta'
  | '\\gamma'
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

BIG_OP
  : '\\int'
  | '\\sum'
  ;

TRIG_OP
  : '\\sin'
  | '\\cos'
  | '\\tan'
  | '\\sec'
  | '\\csc'
  | '\\cot'
  ;
