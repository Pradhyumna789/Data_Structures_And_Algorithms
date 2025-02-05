def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return b

input = 5
result = fib(input)
print(result)

