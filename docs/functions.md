# Funciones

Una función es un bloque de código que cumple con una tarea específica y que puede reutilizarse mandandose a ejecutar en distintas ocasiones dentro de un programa.

Se utilizan funciones para "modularizar" los programas y así facilitar su mantenimiento.

## Declaración de funciones

Para declarar funciones se utiliza `def` seguido del nombre de la función y sus argumentos

```python
def holaMundo():
  print('Hola mundo')
```

Ahora, cuando deseamos ejecutar la funcion, solo la mandamos llamar

```python
holaMundo()
```

## Docstring o documentacion de la función

La primer linea despues de la definición de la función puede ser una cadena que contiene la documentación de la función.

```python
def holaMundo():
  """Imprime hola mundo."""
  print('Hola mundo')
```

## Funciones con retorno de valor

En Python las funciones aún cuando "parece" que no regresan nada en realidad si lo hacen, y lo que hacen es regresar `None`

```python
print(holaMundo())
>>> Hola Mundo
>>> None
```

Para retornar un valor usamos el `return` dentro de nuestra función

```python
def holaMundo():
  """Retorna la cadena hola mundo."""
  return 'Hola mundo'
```

y este valor podemos imprimirlo o guardarlo en una variable

```python
print(holaMundo())
cadena = holaMundo()
```

## Argumentos con valores por default

Cuando declaramos argumentos para nuestras funciones, estamos indicando que para llamar la función se deben enviar esos valores.

Podemos además, indicar un valor por defecto en caso que uno valor no haya sido enviado.

```python
def saluda(who='Mundo'):
  """Imprime un mensaje de saludo."""
  print('Hola', who)

saluda()
>>> Hola Mundo

saluda('Michelle')
>>> Hola Michelle
```

## Asignación de valores default solo la primera vez

La definición y asignación de los valores default se realiza solo una vez, de modo que si se estan usando como valores default objeto como listas, diccionarios, etc, se podrá tener este problema

```python
def agrega(valor, lista=[]):
    lista.append(valor)
    return lista

print(agrega(1))
print(agrega(2))
print(agrega(3))

# La salida sera

>>> [1]
>>> [1, 2]
>>> [1, 2, 3]
```

## Argumentos por posición o por keyword

La manera en que enviamos argumentos a nuestras funciones es por el orden en que estos fueron declarados.

```python
def myFunction(a=1, b='algo', c=3, d='algo mas'):
  print(a,b,c,d)

myFunction(1,2,3,4)
# a = 1
# b = 2
# c = 3
# d = 4
```

Sin embargo, python ofrece la oportunidad de enviar los argumentos usando keywords, es decir, los nombres de las variables.

```python
myFunction(1, d='valor para d', b='bbb')
# a = 1   
# b = bbb
# c = 3
# d = valor para d
```

## Argumentos arbitrarios

Se puede guardar una lista con todos los argumentos que se reciban y de esta manera no indicar la cantidad de argumentos esperados

```python
def invitados(*args):
  for person in args:
    print(person)
```

De esta manera se puede mandar a llamar `invitados('maria', 'pedro', 'pablo')` o con la cantidad de argumentos que se quiera.
