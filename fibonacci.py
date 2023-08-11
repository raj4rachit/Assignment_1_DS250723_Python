limit = int(input("Enter the Number for generating Fibonacci series: "))
fib_series = [0, 1]
series = ''
while fib_series[-1] + fib_series[-2] <= limit:
    fib_series.append(fib_series[-1] + fib_series[-2])

fib_series = fib_series[1:]
fibonacci_string = ' '.join(map(str, fib_series))
print(f"Fibonacci series between 0 to {limit}: {fibonacci_string}")