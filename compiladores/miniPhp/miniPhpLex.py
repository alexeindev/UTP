import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words
    'ARRAY',
    'AS',
    'BREAK',
    'CASE',
    'CATCH',
    'CLASS',
    'CONTINUE',
    'DIE',
    'DO',
    'DUMP',
    'ECHO',
    'ELSE',
    'FALSE',
    'FOR',
    'ENDFOR',
    'FOREACH',
    'FUNCTION',
    'IF',
    'NOT',
    'NEW',
    'OBJECT',
    'PRINT',
    'PRIVATE',
    'PUBLIC',
    'RETURN',
    'SWITCH',
    'THIS',
    'TRUE',
    'VAR',
    'WHILE',
    'DOLLARSIGN',
    'ATSIGN',
    'QUESTIONMARK',
    'ATSIGN',
    'PERCENT',

   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'EQUALEQUAL',
    'OPENPHP',
    'CLOSEPHP',
    'DOT',
    'SEMICOLON',
    'COMMA',
    'DOUBLEQUOTES',
    'SINGLEQUOTES',
    'HASH',
    'GREATER',
    'GREATEREQUAL',
    'DEQUAL',
    'LESS',
    'LESSEQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'UNDERSCORE',
    'LBLOCK',
    'RBLOCK',
    'AND',
    'OR',
    'XOR',

    # Others   
    'ID', 
    'NUMBER',
    'TXT',
)

# Regular expressions rules for a simple tokens 

t_PLUS =r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DOT = r'\.'
t_SEMICOLON =r';'
t_COMMA =r'\,'
t_DOUBLEQUOTES = r'\"'
t_SINGLEQUOTES = r'\''
t_HASH = r'\#'
t_GREATER =r'>'
t_LESS = r'<'
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_UNDERSCORE = r'\_'
t_LBLOCK   = r'{'
t_RBLOCK = r'}'
t_DOLLARSIGN = r'\$'
t_ATSIGN = r'\@'
t_QUESTIONMARK = r'\?'
t_PERCENT = r'\%'

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DIE(t):
    r'die'
    return t

def t_DO(t):
    r'do'
    return t

def t_DUMP(t):
    r'dump'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_FOR(t):
    r'for'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_NOT(t):
	r'not'
	return t

def t_NEW(t):
    r'new'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_PRINT(t):
	r'print'
	return t

def t_PRIVATE(t):
	r'private'
	return t

def t_PUBLIC(t):
	r'public'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THIS(t):
	r'this'
	return t

def t_TRUE(t):
	r'true'
	return t

def t_VAR(t):
	r'var'
	return t
	
def t_WHILE(t):
	r'while'
	return t

def t_ID(t):
    r'\$\w+(_\d\w)*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_EQUAL(t):
	r'='
	return t

def t_EQUALEQUAL(t):
	r'==='
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t
    
def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_MINUSMINUS(t):
	r'--'
	return t

def t_OPENPHP(t):
	r'<\?php'
	return t

def t_CLOSEPHP(t):
	r'\?>'
	return t

def t_AND(t):
	r'(&&)|(and)'
	return t

def t_OR(t):
	r'(\|\|)|(or)'
	return t

def t_XOR(t):
	r'xor'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_slcomments(t):
    r'\#(.|\n)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'test.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
