def overlapping(list1, list2):
    return bool(set(list1) & set(list2))

list1 = input("Enter elements of first list (space separated): ").split()
list2 = input("Enter elements of second list (space separated): ").split()

result = overlapping(list1, list2)

if result:
    print("True : The lists have at least one common element.")
else:
    print("False : The lists don't have any common element.")
