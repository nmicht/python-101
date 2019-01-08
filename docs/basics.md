## Comentarios

Los comentarios en python se ponen con el símbolo de numeral

```python
# Este es un comentario de linea completo
var1 = 5 # Este es un comentario despues de la declaracion de una variable
texto = "#Esta es una cadena" # Este es otro comentario, y la cadena definida, se va a reconocer apesar de tener un numeral
```

## Variables

Una variable es un espacio de memoria que almacena un valor.  
Se considera que una variable no esta definida cuando no tiene un valor asignado.


## Asignación

La asignación de valores a variables se hace con el operador `=`

```python
a = 5
```

Pero también existe la asignación simultánea:

```python
a, b = 0, 1
```

donde `a` recibe el valor `0` y `b` recibe el valor `1`.

## Imprimir información

`print` se utiliza para enviar salidas y al final del print python envia un salto de linea.

```python
myVar = 5
print(myVar)
>>> 5
```

Las cadenas se enviar como tal, entre comillas simples o dobles.

```python
print('Un mensaje')
>>> "Un mensaje"
```

Se pueden enviar distintos valores a imprimir separando por comas, y python por automático agregará un espacio.

```python
myVar = 5
print('El valor de la variable es:', myVar)
>>> "El valor de la variable es: 5"
```

Para evitar el salto de linea se puede usar `end`

```python
myVar = 5
print('El valor de la variable es:', myVar)
print('El doble es:', myVar*2)
>>> "El valor de la variable es: 5"
"El doble es: 10"

print('El valor de la variable es:', myVar, end=', ')
print('El doble es:', myVar*2)
>>> "El valor de la variable es: 5, El doble es: 10"
```

## Obtener entradas del usuario

Para leer información que el usuario introduce a través de la entrada estándar (teclado) podemos usar `input`

```python
n = input('Escribe tu nombre: ') # Deja el prompt listo para que el usuario introduzca datos
```
