grammar TinyGP;

program: statement*;

statement: loopStatement
         | conditionalStatement
         | compoundStatement
         | assignmentStatement
         | inputStatement
         | outputStatement
         | constant;

loopStatement: 'while' '(' condition ')' compoundStatement;

conditionalStatement: 'if' '(' condition ')' compoundStatement ('else' compoundStatement)?;

compoundStatement: '{' statement* '}';

assignmentStatement: variable '=' (expression | condition | boolean) (';')? ;

inputStatement: 'input' '(' assignmentStatement ')' ';';

outputStatement: 'output' '(' expression ')' ';';

//condition: expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression (('&&' | '||') condition)* | boolean ('&&' | '||') boolean (('&&' | '||') condition)*;
condition: expressionCondition (('&&' | '||') (expressionCondition | logicCondition))* | logicCondition (('&&' | '||') (expressionCondition | logicCondition))*;

expressionCondition: expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression;

logicCondition: boolean ('==' | '!=') boolean;

expression: ('-')? term (('+' | '-') term)*;

term: factor (('*' | '/') factor)*;

factor: '(' expression ')'
      | variable
      | NUMBER;

variable: ID;

constant: 'const' ID '=' expression ';' ;

ID: [a-zA-Z][a-zA-Z0-9]*;

NUMBER: ([0-9]+);

boolean: 'true' | 'false';

WS: [ \t\r\n]+ -> skip;