import ply.lex as lex
import sys

tokens = [
    #RESERVE WORDS
    'BREAK', 'CLONE', 'FINAL', 'GLOBAL', 'INCLUDE_ONCE', 'LIST', 'PRIVATE',
    'PRINT', 'ECHO', 'ARRAY', 'FOR', 'IF','WHILE','DO',
    'ELSE','SWITCH', 'ENDSWITCH', 'CASE', 'OBJECT','CLASS',
    'PUBLIC', 'THIS', 'NEW', 'VAR', 'DUMP','FUNCTION',
    'RETURN', 'TRUE', 'FALSE', 'AND','OR','NOT',

    #SYMBOLS
    'PLUS','PLUSPLUS','MINUS','MINUSMINUS','TIMES',
    'DIVIDE','OPENPHP','CLOSEPHP','DOT','SEMICOLON',
    'COMMA','DOUBLEQUOTES','SINGLEQUOTES','HASH',
    'EQUAL','GREATER','GREATEREQUAL','EQUALEQUAL', 
    'DISTINT', 'LESS', 'LESSEQUAL', 'LPARENTHESIS', 'RPARENTHESIS', 'LSQUAREBRACKET',
    'RSQUAREBRACKET','UNDERSCORE','LCURLYBRACKET','RCURLYBRACKET',
    
    #COMMENTS & QUOTES
    'SLCOMMENT','MLCOMMENT',
    
    #OTHERS
    'ID',
    'NUMBER',

         ]

t_ignore  = r'\t'
t_PLUS =r'\+'
t_PLUSPLUS= r'\++'
t_EQUAL = r'='
t_EQUALEQUAL = '=='
t_TIMES = r'\*'
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_DIVIDE = r'/'
t_OPENPHP = r'<\?php'
t_CLOSEPHP = r'\?>'
t_DOT = r'\.'
t_SEMICOLON =r';'
t_COMMA =r'\,'
t_DOUBLEQUOTES = r'\"'
t_SINGLEQUOTES = r'\''
t_HASH = r'\#'
t_GREATER =r'>'
t_GREATEREQUAL = r'>='
t_DISTINT = r'!='
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_UNDERSCORE = r'\_'
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'

def t_ID(t):
    r'$\w+(_\d\w )*'
    return t 

def t_SLCOMMENT(t):
    r'\#.*'
    return t

def t_MLCOMMENT(t):
    r'/\*\*(.|\n)*?\*/'
    return t

def t_NUMBER(t):
    r'(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d+)? | (\d+[Ee][+-]?\d+)'
    return t

def t_error(t):
    print ("caracter invalido o ilegal %s" %t.value[0])
    t.lexer.skip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo =''
    respuesta = False
    cont = 1


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
	test(data,lexer)
	input()





