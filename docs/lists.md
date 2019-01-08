# Listas

En Python las listas son arreglos que pueden contener cualquier tipo de dato,
pero se espera que idealmente sea una colección del mismo tipo.

```python
myList = [1,2,3,4,5]
abc = ['a','b','c','d','e']
```

## Acceder a elementos de la lista

Se puede acceder a los elementos a través de su indice que comienza en cero.

```python
myList = [1,2,3,4,5]
myList[2]
>>> 3
```

También se tienen los indices negativos que comienzan en -1 y se usan para acceder a las posiciones a la inversa

```python
myList = [1,2,3,4,5]
myList[-2]
>>> 4
```

## Porciones de la lista

Para obtener porciones de una lista se indica el indice para comenzar y el indice al que se quiere llegar (sin incluir).  
Python hará un `shadow copy`, es decir, va a evitar repetir cosas, por lo que en caso de existir referencias, las usará en lugar de copiar los valores.

```python
myList = [1,2,3,4,5]
myList[0:3] # Desde la posición cero hasta 2
>>> [1,2,3]
```

Permite el uso de índices negativos.

```python
myList = [1,2,3,4,5]
myList[-2:] # Desde la posición -2 hasta el final de la lista
>>> [4,5]
```

## Concatenación de listas

Para concatenar listas se utiliza el operador `+`

```python
list1 = [1,2,3,4,5]
list2 = [11,12,13,14]
list3 = list1 + list2
>>> [1, 2, 3, 4, 5, 11, 12, 13, 14]
```

## Modificar una lista

### Por su indice
Se puede modificar una posición directa de la lista a través de su indice

```python
myList = [1,2,3,4,5]
myList[0] = 0
>>> [0,2,3,4,5]
```

### Agregar un elemento al final de la lista

Se pueden agregar nuevos elementos al final de la lista con `append`

```python
myList = [1,2,3,4,5]
myList.append(10)
>>> [1,2,3,4,5,10]
```

### Modificar una porcion de la lista

Pero también se pueden hacer cambios mas complejos como obtener una porción de la lista y reemplazarlo por otra lista, de este modo, agregando mas elementos.

```python
myList = [1,2,3,4,5]
myList[0:1] = [0,1]
>>> [0,1,2,3,4,5]
```

### Eliminar una porcion de la lista

Se puede eliminar una porcion de la lista simplmente asignandola a vacio.

```python
myList = [1,2,3,4,5]
myList[1:3] = []
>>> [1,4,5]
```

## Tamaño de una lista

Para conocer el tamaño de una lista se utiliza el método `len`

```python
myList = [1,2,3,4,5]
len(myList)
>>> 5
```

## Listas de listas

Conociendo todos estos términos básicos de las listas ahora es fácil manipular listas de Listas


```python
myList = [1,2,3,4,5]
myList[0] = [1,2,3]
>>> [[1,2,3],2,3,4,5]
```
