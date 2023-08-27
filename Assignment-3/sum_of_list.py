def sumOfList(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Take input from the user
num_count = int(input("Enter the number of elements: "))
numbers_list = []
for i in range(num_count):
    num = int(input(f"Enter number {i+1}: "))
    numbers_list.append(num)

result = sumOfList(numbers_list)
print(f"Sum of List {numbers_list}: {result}")
