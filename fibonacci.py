while True:
    limit = input("Enter the Number for generating Fibonacci series: ")
    if limit.strip():  # Check if the input is not empty after stripping whitespace
        try:
            limit = int(limit)
            break  # Break the loop if a valid integer is provided
        except ValueError:
            print("Please enter a valid integer.")
    else:
        print("Input cannot be empty.")

fib_series = [0, 1]

while fib_series[-1] + fib_series[-2] <= limit:
    fib_series.append(fib_series[-1] + fib_series[-2])

fib_series = fib_series[1:]
fibonacci_string = ' '.join(map(str, fib_series))
print(f"Fibonacci series between 0 to {limit}: {fibonacci_string}")