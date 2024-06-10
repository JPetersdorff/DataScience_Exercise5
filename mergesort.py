def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot the initial list
plt.figure(figsize=(12, 6))

# create subplot to  visualize both lists in one plotting window
plt.subplot(1, 2, 1)
plt.plot(range(len(my_list)), my_list, marker='o', linestyle='-', color='b', label='Initial List')
plt.title('Initial List')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# Perform merge sort
mergeSort(my_list)

# Plot the sorted list
plt.subplot(1, 2, 2)
plt.plot(range(len(my_list)), my_list, marker='o', linestyle='-', color='g', label='Sorted List')
plt.title('Sorted List')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# add title, show plots
plt.suptitle('Merge Sort Visualization')
plt.show()