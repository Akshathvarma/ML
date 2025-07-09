list1_input = input("Enter elements of list 1 (separated by spaces): ")
list1_input_split = list1_input.split()
list1_converted = map(int, list1_input_split)
list1 = list(list1_converted)

list2_input = input("Enter elements of list 2 (separated by spaces): ")
list2_input_split = list2_input.split()
list2_converted = map(int, list2_input_split)
list2 = list(list2_converted)

common_elements = []
for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print("Number of common elements:", len(common_elements))
