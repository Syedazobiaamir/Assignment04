def get_first_element(lst):
    print(lst[0])

# Prompt user to input the list
n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    lst.append(element)

get_first_element(lst)
