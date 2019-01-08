# Fibonacci sequence
a, b = 0, 1
while(a < 10):
    print(a, end=', ') # Avoid with end the breakline
    a, b = b, a+b
else:
    print(a, 'is not less than 10')

print('Program ended')
