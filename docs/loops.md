# 6.2 Ciclos

En programación, un ciclo es un bloque de código que se repetirá en distintas ocasiones siempre y cuando en cada iteración se cumpla una condición.

## While

Un ciclo while evalua primero si una condición se cumple, y en caso de que se cumpla, entonces ejecuta el código que se encuentra dentro del bloque y regresa a la condición.
Se vuelve a evaluar la condición y si es verdadero, se vuelve a ejecutar el código que se encuentra dentro del bloque.

```python
i = 1
while(i <= 5):
  print('Iteracion', i)
  i += 1

```

## Else en el while

A diferencia de otros lenguajes, python permite agregar una condición `else` al while, permitiendo ejecutar cierto código en caso de que no se cumpla la condición antes de salir del ciclo.

```python
i = 1
while(i <= 5):
  print('Iteracion', i)
  i += 1
else:
  print(i, 'ya no cumple la condicion')

```

# Break

Cuando se desea romper un ciclo por completo se utiliza el `break`

```python
i = 1
while(i <= 5):
  if(i == 2):
    break
  print('Iteracion', i)
  i += 1

```

En este ejemplo, a pesar de tener un ciclo que debería iterar desde 1 hasta 5, cuando llega a 2, se termina.

# Continue

El `continue` nos permite romper solo una iteración del ciclo, es decir, si queremos continuar con el ciclo, pero no seguir con el proceso actual, se usar continue.

```python
i = 0
while(i < 5):
  i += 1
  if(i % 2):
    continue
  print('Iteracion', i)

```

En este caso tenemos un ciclo que itera de 0 a 4, lo incrementa, y lo imprime, pero hemos agregado una condición para que si el número es múltiplo de 2, entonces termine la iteración y no siga con la ejecución.

# For

El ciclo `for` en python se utiliza para iterar sobre una secuencia (listas por ejemplo) lo cual lo convierte en lo similar a un `foreach` de otros lenguajes.

```python
mascotas = ['gato', 'perro', 'pez']
for animal in mascotas:
  print('Yo tengo un', animal)

>>> Yo tengo un gato
>>> Yo tengo un perro
>>> Yo tengo un pez
```

## Else en el for

Al igual que con el while, en python se puede agregar una condición else

```python
mascotas = ['gato', 'perro', 'pez']
for animal in mascotas:
  print('Yo tengo un', animal)
else:
  print('Ya no se puede iterar, pero el ultimo animal fue:', animal)

>>> Yo tengo un gato
>>> Yo tengo un perro
>>> Yo tengo un pez
>>> Ya no se puede iterar, pero el ultimo animal fue: pez
```

# Modificar la secuencia mientras se itera

En un for no se hace copia de los valores, de modo que si quieres modificar la secuencia, se recomienda que primero hagas una copia.
Recuerda que puedes usar la notación `"slice"`, es decir `[n:x]`.

# Iterar sobre una secuencia de números

`range` es un método de python que nos permite generar una serie de la cantidad de números que le indiquemos, pero en realidad no es una lista como tal, es decir, no guarda nada en memoria, y esos elementos existen solo cuando los iteramos.

```python
x = range(5)
>>> range(0, 5)
```

Como vemos en el ejemplo, si imprimimos `x` lo que devuelve es `range(0,5)` pero no hay datos.

Sin embargo, cuando iteramos un rango, entonces los valores si existen.

```python
for i in range(5):
  print(i)

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
```

# Algunas técnicas de iteración

Con todas las facilidades de python, se puede lograr combinar técnicas para iterar y manipular secuencias.

Iteramos una lista e imprimos los elementos de la lista, pero también su índice.

```python
mascotas = ['gato', 'perro', 'pez']
for i in range(len(mascotas)):
  print(i, mascotas[i])

>>> 0 gato
>>> 1 perro
>>> 2 pez
```

[:arrow_forward: Siguiente: Funciones](functions.md)
