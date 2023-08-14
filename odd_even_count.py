def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

try:
    num_series = input("Enter a series of numbers separated by spaces: ")
    num_list = [int(x) for x in num_series.split()]

    even_count, odd_count = count_even_odd(num_list)

    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)

except ValueError:
    print("Invalid input. Please enter a valid series of numbers.")
