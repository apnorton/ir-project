doc : tex '\n';

tex 
  : tex '+' term | tex '+'
  | tex '-' term | tex '-'
  | tex REL tex
  ;

term 
  : factor | term factor
  | term MUL factor
  | term DIV factor
  ;

factor : pack | factor '!' | factor script;

pack : atom
  | '(' tex ')' | '(' tex ']'
  | '[' tex ')' | '[' tex ']'
  ;

script 
  : '_' atom | '^' atom
  | '_' atom '^' atom
  | '^' atom '_' atom
  ;

