import ply.yacc as yacc
from analizadorlexico import tokens
import analizadorlexico
import sys

VERBOSE = 1

def p_PHP(p):
		'PHP :OPENPHP declaration_list CLOSEPHP'
		pass

def p_declaration_list_1(p):
		'declaration_list : declaration_list  declaration' 
		pass

def p_declaration_list_2(p):
		'declaration_list : declaration'
		pass

def p_declaration(p):
		'''declaration : var_declaration
					  			| fun_declaration
					  			| header_declaration'''
		pass

def p_header_declaration_1(p):
		'''header_declaration : DEFINE LPAREN DOUBLEQUOTES VARIABLE DOUBLEQUOTES COMMA TXT RPAREN SEMICOLON
								| DEFINE LPAREN SINGLEQUOTES VARIABLE SINGLEQUOTES COMMA TXT RPAREN SEMICOLON'''
		pass

def p_header_declaration_2(p):
		'''header_declaration : DEFINE LPAREN DOUBLEQUOTES VARIABLE DOUBLEQUOTES COMMA NUMBER RPAREN SEMICOLON
								| DEFINE LPAREN SINGLEQUOTES VARIABLE SINGLEQUOTES COMMA NUMBER RPAREN SEMICOLON'''
		pass

def p_var_declaration_1(p):
		'var_declaration : var_declaration2 SEMICOLON'
		pass

def p_var_declaration_2(p):
		'''var_declaration2 : ID COMMA var_declaration2
														| ID
														| ID LBRACKET NUMBER RBRACKET COMMA var_declaration2
														| ID LBRACKET NUMBER RBRACKET 
														| ID EQUAL TXT COMMA var_declaration2
														| ID EQUAL TXT
														| ID EQUAL var_declaration2
														| ID EQUAL AMPERSANT ID COMMA var_declaration2
														| ID EQUAL AMPERSANT ID 
														| ID EQUAL simple_expresion COMMA var_declaration2
														| ID EQUAL simple_expresion '''
		pass


def p_fun_declaration(p):
		'fun_declaration : FUNCTION VARIABLE LPAREN params RPAREN compount_stmt'
		pass

def p_params_1(p):
		'params : var_declaration2'
		pass

def p_params_2(p):
		'params : empty'
		pass

def p_compount_stmt(p):
		'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
		pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

def p_statement(p):
	'''statement : expression_stmt
				| writing_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt'''
	pass

def p_statement_block_1(p):
  'statement_block : LBLOCK statement_list RBLOCK'
	pass 

def p_statement_block_2(p):
    'statemenet_block: statemenet'
	pass 


def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_writing_stmt_1(p):
	'''writing_stmt : ECHO TXT SEMICOLON
					| ECHO NUMBER SEMICOLON
					| ECHO ID SEMICOLON
					'''
	pass				
def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement_block'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statemenet_block ELSE statemenet_block'
	pass

def p_selection_stmt_3(p):
    'selection_stmt : SWITCH LPAREN var RPAREN statemenet'
	pass 

def p_selection_stmt_4(p):
    'selection_stmt : CASE NUMBER COLON statemenet BREAK SEMICOLON'
	pass 

def p_selection_stmt_5(p):
    'selection_ : DEFAULT COLON statemenet BREAK SEMICOLON'
	pass 


def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement_block'
	pass


def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement_block'
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var EQUAL AMPERSANT VARIABLE'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET ID RBRACKET'
	pass

def p_var_3(p):
    'var : ID LBRACKET NUMBER RBRACKET'
	pass 

def p_var_4(p):
    'var : ID LBRACKET expression RBRACKET '
	pass 


def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : LESS  
			| LESSEQUAL 
			| GREATER 
			| GREATEREQUAL
			| DEQUAL 
			| DISTINT
			| EQUALEQUAL 
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term
                                              
        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_addop(p):
	'''addop : PLUS 
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER' 
	pass

def p_factor_5(p):
    'factor : VARIABLE'
	pass

def p_call(p):
	'call : VARIABLE LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.php'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("El analizador sintactico dice que esta correcto")
	#input()
