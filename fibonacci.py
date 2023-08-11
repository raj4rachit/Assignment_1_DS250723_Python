limit = 50
fib_series = [0, 1]
while fib_series[-1] + fib_series[-2] <= limit:
    fib_series.append(fib_series[-1] + fib_series[-2])

print(f"Fibonacci series up to {limit}: {fib_series}")
