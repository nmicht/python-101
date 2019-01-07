# Fibonacci sequence
a, b = 0, 1
while(a < 10):
    print(a, end=', ') # Avoid with end the breakline
    a, b = b, a+b

print('Program ended')
