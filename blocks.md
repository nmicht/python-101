# Blocks

In python the blocks are defined by indentation, no need of curly braces.

```python
# Fibonacci sequence
a, b = 0, 1
while(a < 10):
    print(a)
    a, b = b, a+b
```

In this example, the block for the while starts with `:` and all the block is indented.

In case we need more code after the block, a blank line is needed.

```python
# Fibonacci sequence
a, b = 0, 1
while(a < 10):
    print(a)
    a, b = b, a+b

print('Program ended')
```
