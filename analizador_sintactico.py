import ply.yacc as yacc
from analizador_lexico import tokens

def p_program(p):
    '''
    program : statements
    '''
    p[0] = "Programa válido."

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

def p_statement(p):
    '''
    statement : expression SEMICOLON
              | for_loop
              | println_statement
    '''
    p[0] = "Declaración válida."

def p_for_loop(p):
    '''
    for_loop : FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN LEFT_BRACE statements RIGHT_BRACE
    '''
    p[0] = "Bucle For válido."

def p_println_statement(p):
    '''
    println_statement : SYSTEM DOT OUT DOT PRINTLN LPAREN expression RPAREN SEMICOLON
    '''
    p[0] = "Declaración de impresión válida."

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = "Asignación válida."

def p_condition(p):
    '''
    condition : expression
    '''
    p[0] = "Condición válida."

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | ID
               | NUMBER
               | INCREMENT
               | STRING
               | expression LESS_THAN expression
               | expression GREATER_THAN expression
               | expression LESS_THAN_EQUAL expression
               | expression GREATER_THAN_EQUAL expression
               | expression EQUAL_EQUAL expression
               | expression NOT_EQUAL expression
    '''
    p[0] = "Expresión válida."

def p_increment(p):
    '''
    increment : ID INCREMENT
    '''
    p[0] = "Incremento válido."

def p_error(p):
    if p is not None:
        mensaje_error = f"Error de sintaxis en el token '{p.value}', tipo '{p.type}' en la línea {p.lineno}"
        raise SyntaxError(mensaje_error)
    else:
        raise SyntaxError("Error de sintaxis: No se pudo construir el árbol de análisis.")

parser = yacc.yacc(errorlog=yacc.NullLogger())


def parse_code(code, debug=None):
    try:
        parser.parse(code, debug=debug)
        resultado_sintactico = {"status": "success", "message": "Análisis sintáctico exitoso"}
    except SyntaxError as e:
        resultado_sintactico = {"status": "error", "message": str(e)}
        if debug:
            debug.append(resultado_sintactico)  

    return resultado_sintactico