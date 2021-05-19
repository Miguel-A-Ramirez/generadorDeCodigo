# Convertidor de notacion infija a ensamblador

## Descripción:
Programa sencillo hecho en python 3 donde se recibe por terminal una notacion infija, lo pasa a una lista de tokens, despues lo convierte a una expresion posfija, genera el codigo intermedio y finalmente lo convierte a codigo ensamblador.

## Ejemplo de funcionamiento:
**Ingresar cadena de operaciones infija:**
a+b-c*d

**la cadena original es:** 
a+b-c*d

**la lista de tokens de la cadena es**:  
['a', '+', 'b', '-', 'c', '*', 'd']

**la expresion posfija es:**  
['a', 'b', '+', 'c', 'd', '*', '-']

**el codigo intermedio es:**
t1=a+b;
t2=c*d;
t3=t1-t2;

**el codigo ensamblador es:**
LDA a;
ADD b;
STA t1;
LDA c;
MUL d;
STA t2;
LDA t1;
SUB t2;
STA t3;
