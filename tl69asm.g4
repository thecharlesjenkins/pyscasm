grammar tl69asm;

tl69asmProg: (tl69asmLine EOL)* tl69asmLine EOL? EOF;

tl69asmLine: label? (directive|instruction)? comment?;
label: ID COLON;

directive: (directiveDW | directiveORG | directiveEQU);
directiveDW: DIR_DW expr;
directiveORG: DIR_ORG expr;
directiveEQU: label DIR_EQU expr;

operands: | operand (COMMA operand)* ;
instruction: OpCode operands;

expr: (integer | labelRef);
operand: (integer | register | labelRef);


labelRef: ID;
register: Register;
integer: INT_HEX | INT_DEC | INT_BIN | INT_OCT;
INT_HEX: SUB? ('0x'|'0X'|'&H'|'&h')[0-9A-Fa-f]+;
INT_BIN: SUB? ('0b'|'&b'|'&B')[0-1]+;
INT_OCT: SUB? ('&O'|'&o')[0-7]+;
INT_DEC: SUB? [0-9]+;

White_Space: [ \t]+ -> skip;
EOL: [\r\n]+;
COLON: ':';
LPARN: '(';
RPARN: ')';
COMMA: ',';
ADD: '+';
SUB: '-';

fragment A : [aA]; // match either an 'a' or 'A'
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

DIR_EQU: E Q U;
DIR_DW: D W;
DIR_ORG: O R G;

Register: [rR][0-9]* | S P | B P;

OpCode: ALUOps
| ControlFlowOps
| IOOps
| MemoryOps;

fragment ALUOps: OpADDI
| OpADD
| OpSUBI
| OpSUB
| OpMULI
| OpMUL
| OpXCHG
| OpCMPI
| OpCMP
| OpORI
| OpOR
| OpXORI
| OpXOR
| OpANDI
| OpAND
| OpNOT;

fragment ControlFlowOps:
Jumps
| FunctionCallOps
| OpHALT
;

fragment IOOps: OpOUT
| OpIN;

OpADDI: A D D I;
OpADD: A D D;
OpSUBI: S U B I;
OpSUB: S U B;
OpMULI: M U L I;
OpMUL: M U L;
OpXCHG: X C H G;
OpCMPI: C M P I;
OpCMP: C M P;
OpORI: O R I;
OpOR: O R;
OpXORI: X O R I;
OpXOR: X O R;
OpANDI: A N D I;
OpAND: A N D;
OpNOT: N O T;

OpOUT: O U T;
OpIN: I N;

fragment Jumps : OpJO
| OpJNO
| OpJS
| OpJNS
| OpJE
| OpJNE
| OpJB
| OpJNB
| OpJBE
| OpJA
| OpJL
| OpJGE
| OpJLE
| OpJG
| OpJMP;

OpJO: J O;
OpJNO: J N O;
OpJS: J S;
OpJNS: J N S;
OpJE: J E;
OpJNE: J N E;
OpJB: J B;
OpJNB: J N B;
OpJBE: J B E;
OpJA: J A;
OpJL: J L;
OpJGE: J G E;
OpJLE: J L E;
OpJG: J G;
OpJMP: J M P;

fragment FunctionCallOps: OpCALL
| OpRET;

OpCALL: C A L L;
OpRET: R E T;

fragment MemoryOps: OpPUSH
| OpPOP
| OpLW
| OpSW;

OpPUSH: P U S H;
OpPOP: P O P;
OpLW: L W;
OpSW: S W;

OpHALT: H A L T;

ID: [a-zA-Z_$%][a-zA-Z0-9_$%]*;

comment: COMMENT;

COMMENT: ';' ~ [\r\n]* -> skip;
DOUBLE_SLASH_COMMENT: '//'~[\r\n]* -> skip;
WHITESPACE: [ \t] -> skip;
