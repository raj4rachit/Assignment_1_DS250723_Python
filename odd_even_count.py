def countOddEvenNumbers(numbers):
    evenCount = 0
    oddCount = 0

    for num in numbers:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return evenCount, oddCount

try:
    num_series = input("Enter a series of numbers separated by spaces: ")
    num_list = [int(x) for x in num_series.split()]

    evenCount, oddCount = countOddEvenNumbers(num_list)

    print("Number of even numbers: ", evenCount)
    print("Number of odd numbers: ", oddCount)

except ValueError:
    print("Invalid input. Please enter a valid series of numbers.")
