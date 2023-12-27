grammar TinyGP;
///usunac ; ??
program: statement*;

statement: loopStatement
         | conditionalStatement
         | compoundStatement
         | assignmentStatement
         | inputStatement
         | outputStatement;

loopStatement: 'while'  condition  compoundStatement; ////usunelam nawiasy

conditionalStatement: 'if'  condition compoundStatement ('else' compoundStatement)?;

compoundStatement: '{' statement* '}';

assignmentStatement: variable '='  (condition | expression | inputStatement) (';')? ;

inputStatement: 'input()' (';')?;

outputStatement: 'output' '(' (variable | NUMBER) ')' (';')?;

condition: ('(')(expressionCondition ) (('&&' | '||') (expressionCondition ))* (')');
expressionCondition: expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression;

expression: ('-')? term (('+' | '-') term)*;

term: factor (('*' | '/') factor)*;

factor: '(' expression ')'
      | variable
      | boolean
      | NUMBER;

variable: ID;

ID: [a-zA-Z][a-zA-Z0-9_]*;

NUMBER:('-')? ([0-9]+.[0-9]+);

boolean: 'true' | 'false';

WS: [ \t\r\n]+ -> skip;