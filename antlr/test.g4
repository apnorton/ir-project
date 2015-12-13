grammar test;

r : '(' r ')' r | NULL;
NULL : '' ? EOF;
WS : [ \t\r\n]+ -> skip;
