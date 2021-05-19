# -*- coding: cp1252 -*-

def obtenerPrioridadOperador(o):
    # Función que trabaja con convertirInfijaA**.
    return {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}.get(o)

def listaDeTokens(texto):
    '''Dado un texto de código completo, devuelve todos sus tokens.'''
    token = ""
    listaTokens = []
    for i in texto:
        if esSeparador(i) and token != "":
            listaTokens.append(token)
            token = ""
        elif esSimbEsp(i):
            if token != "":
                listaTokens.append(token)
                token = ""
            listaTokens.append(i)
        elif not (esSeparador(i)):
            token += i
    return listaTokens

def obtenerListaInfija(cadena_infija):
    '''Devuelve una cadena en notación infija dividida por sus elementos.'''
    infija = []
    cad = ''
    for i in cadena_infija:
       if i in['+', '-', '*', '/', '(', ')', '^']:
           if cad != '':
               infija.append(cad)
               cad = ''
           infija.append(i)
       elif i == chr(32): # Si es un espacio.
           cad = cad
       else:
           cad += i
    if cad != '':
       infija.append(cad)
    return infija

def convertirInfijaAPostfija(expresion_infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    infija = obtenerListaInfija(expresion_infija)
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and (obtenerPrioridadOperador(e)) <= obtenerPrioridadOperador(pila[len(pila) - 1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida

def getCodigoIntermedio(expresion_posfija):
    '''Si la posfija tiene valores, recibe la lista Posfija y devuelve el resultado.'''
    ope={"+":"ADD","-":"SUB","*":"MUL","/":"DIV"}
    codInt = []
    pila = []
    t = 1
    for i in expresion_posfija:
        if not(i in ['+', '-', '*', '/']):
            pila.append(i)            
        else:
            variable = "t"+str(t)
            op2 = pila.pop()            
            op1 = pila.pop()            
            cad = variable+"="+op1 + i + op2+";"
            pila.append(variable)
            codInt.append(cad)
            #codigo agregado:
            codigo.append("LDA "+op1+";")
            codigo.append(ope[i]+" "+op2+";")
            codigo.append("STA "+variable+";")
            t = t+1            
    return codInt

codigo=[]

print("Ingresar cadena de operaciones infija")
cadena1 = input()

print ("la cadena original es: "+ cadena1)

# convierte la cadena en una lista de tokens
tokens = obtenerListaInfija(cadena1)
print("\nla lista de tokens de la cadena es: ",tokens)

# convierte de infija a posfija
posfija = convertirInfijaAPostfija(tokens)
print ("\nla expresion posfija es: ",posfija)

#Genera el código intermedio y lo imprime
print("\nel codigo intermedio es:")
codigoInter = getCodigoIntermedio(posfija)
for c in codigoInter:
    print (c)

#Genera el codigo ensamblador y lo imprime
print("\nel codigo ensamblador es:")
for i in codigo:
    print(i)
