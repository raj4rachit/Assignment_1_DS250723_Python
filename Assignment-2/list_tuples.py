def sort_tuples_by_last_element(tuple_list):
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            if tuple_list[i][-1] > tuple_list[j][-1]:
                tuple_list[i], tuple_list[j] = tuple_list[j], tuple_list[i]
    return tuple_list

# Get user input for the number of tuples
num_tuples = int(input("Enter the number of tuples: "))
input_tuples = []

# Get user input for each tuple
for i in range(num_tuples):
    tuple_values = tuple(map(int, input(f"Enter values for tuple {i+1} (comma-separated): ").split(',')))
    input_tuples.append(tuple_values)

sorted_tuples = sort_tuples_by_last_element(input_tuples)
print("Sorted tuples:", sorted_tuples)