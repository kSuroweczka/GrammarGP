# GrammarGP
## Overview
The aim of the project is to find the best solution to a given problem using genetic programming. Found best individual is written in language that is specially created for that purpose. 

## Technologies
- Python
- ANTLR4

## Directories
    Grammar - contains grammar for new programming language, implemented interpreter using ANTLR4
    library - this is where the main part of the program is located. This folder contains 3 subdirectories: Model, Solver, Tasks. 
    The Model is responsible for generating tree programs, the Solver is responsible for generating and evaluating solutions using 
    genetic programming, and the Tasks folder is responsible for generating appropriate data for given problems.
## Grammar
```antlr
grammar TinyGP;
program: statement*;

statement: loopStatement
         | conditionalStatement
         | compoundStatement
         | assignmentStatement
         | inputStatement
         | outputStatement;

loopStatement: 'while'  condition  compoundStatement;

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
```

## Fitness Functions
Each problem has its own fitness function.
