# 6.1 Condicionales

Una condicional es una estructura de control que nos permite ejecutar un bloque de código solo si se cumple una condicional.

```python
if x < 0:
  print('El valor de x es menor a cero')
```

En este ejemplo, se evalua que el valor de la variable x sea menor a cero, y en caso de que esto sea verdadero, entonces ejecutara el código dentro del bloque.

## Sino

En una condicional se busca que se cumpla una condición, pero en caso que esto no ocurra, se puede entonces programar para el caso `sino`

```python
if x < 0:
  print('El valor de x es menor a cero')
else:
  print('El valor de x NO es menor a cero')
```

## Elif

Anidar condiciones es la opción de unir condiciones `if` con sus casos `sino`. Ejemplo "Quiero ir a bailar, sino, si el día no es frío, quiero ir a nadar" esto sería un else y un if, pero en python podemos abreviar con `elif`

```python
if x < 0:
  print('El valor de x es menor a cero')
elif x == 0:
  print('El valor de x es cero')
else:
  print('El valor de x es mayor a cero')
```

En otros lenguajes de programación existe la estructura `switch`, sin embargo en python esta no existe.

[:arrow_forward: Siguiente: Ciclos](loops.md)
