grammar TinyGP;

program: statement*;

statement: loopStatement
         | conditionalStatement
         | compoundStatement
         | assignmentStatement
         | inputStatement
         | outputStatement
         | functionCall;

loopStatement: 'while' '(' condition ')' compoundStatement;

conditionalStatement: 'if' '(' condition ')' compoundStatement ('else' compoundStatement)?;

compoundStatement: '{' statement* '}';

assignmentStatement: variable ('='|'+='|'-='|'*='|'/=') expression ';' | constant;

inputStatement: 'input' '(' variable ')' ';';

outputStatement: 'output' '(' expression ')' ';';

condition: expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression (('&&' | '||') condition)*;

expression: ('-')? term (('+' | '-') term)*;

term: factor (('*' | '/') factor)*;

factor: '(' expression ')'
      | variable
      | NUMBER
      | boolean
      | functionCall
      | constant ;

functionCall: ID '(' argumentList? ')';

argumentList: expression (',' expression)*;

variable: ID;

constant: 'const' ID '=' expression ';' ;

ID: [a-zA-Z][a-zA-Z0-9]*;

NUMBER: ([0-9]+);

boolean: 'true' | 'false';

WS: [ \t\r\n]+ -> skip;