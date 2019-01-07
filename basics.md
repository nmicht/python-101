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

## Operadores aritméticos

### Suma, resta, multiplicación y división
En python se pueden realizar todas las operaciones básicas conocidas tales como suma, resta, multiplicación y división.

```python
2 + 3
>>> 4
2 * 3
>>> 6
2 - 3
>>> -1
2 / 3
>>> 0.6666666666666666
```

### Residuo

El residuo es la parte restante de una division de enteros

```python
2 % 3
>>> 2
5 % 2
>>> 1
```

### Parte entera de la división

En Python cualquier división siempre devolverá un flotante a pesar de que los inputs sean enteros.

Si por el contrario, lo que se busca es la parte entera, python tiene el operador `//`.

```python
2 // 3
>>> 0
```

### Potencia

```python
2 ** 3
>>> 8
```

## Cadenas

Las cadenas en python se utilizan para caracteres o una secuencia de los mismos.  
Se pueden representar con comillas simples `''` o con comillas dobles `""`.  

```python
'una cadena'
"otra cadena"
```

Existen también cadenas de múltiple linea

```python
print("""\
   Esta es una cadena       con espacios
   y de multiples lineas
que python acepta
""")
```

### Concatenación

El operador `+` se utiliza para concatenar cadenas

```python
'ho' + 'la'
>>> hola
```

Sin embargo, en el ejemplo anterior se puede omitir el símbolo de `+` ya que python concatena por automático cualquier cadena que este contigua a otra.

```python
'ho' 'la'
>>> hola
```

### Repetir cadenas

Si se desea repetir una cadena, se puede realizar una "multiplicación"

```python
3 * 'Yo'
>>> YoYoYo
```

## Manejo de cadenas como secuencias

Python utiliza el tipo de dato secuencia para manipular las cadenas y las listas.

### Acceder a elementos de la cadena por su indice

Los caracteres de una cadena se indexan a partir del cero de izquierda a derecha.  

```python
word = 'Michelle'
word[3]
>>> h
```

Se utiliza también indices negativos para iniciar el conteo desde el final de la cadena. Estos inician en -1.

```python
word = 'Michelle'
word[-2]
>>> l
```

### Modificación de cadenas

**NOTA** Las cadenas no se pueden modificar, por lo cual no se pueden cambiar los valores de una posición.

```python
word = 'Michelle'
word[0] = 'm'
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

### Subcadenas

Para obtener porciones de una cadena se indica el indice para comenzar y el indice al que se quiere llegar (sin incluir).

```python
word = 'Michelle'
word[1:4] # Desde uno hasta 3
>>> ich
```

Se pueden usar tambien indices negativos

```python
word = 'Michelle'
word[-2:] # Desde -2 y hasta el final de la cadena
>>> le
```
