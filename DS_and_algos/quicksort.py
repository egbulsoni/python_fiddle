def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

# Exemplo de uso:
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_list = quicksort(my_list)
print(sorted_list)
