# 4. Cadenas

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

Los operadores de escape como `\n` funcionan tanto con comillas simples como en comillas dobles.

## Concatenación

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

## Repetir cadenas

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

[:arrow_forward: Siguiente: Listas](lists.md)
