# Bloques

En python los bloques de códigos se definen por espacios y no hay necesidad de llaves.

```python
# Secuencia Fibonacci
a, b = 0, 1
while(a < 10):
    print(a)
    a, b = b, a+b
```

En este ejemplo, el bloque inicia con `:` y el contenido del bloque esta indentado.

En caso se que se requiera código después del bloque se agrega una línea en blanco.

```python
# Secuencia Fibonacci
a, b = 0, 1
while(a < 10):
    print(a)
    a, b = b, a+b

print('Termina el programa')
```
