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
