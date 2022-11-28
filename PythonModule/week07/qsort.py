
def partition(array, lindex, rindex):
    pivot = (array[lindex] + array[rindex]) // 2
    i = lindex
    j = rindex
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        i += 1
        j -= 1

def qsort(array, lindex, rindex):
    if lindex < rindex:
        middle = partition(array, lindex, rindex)
        qsort(array, lindex, middle)
        qsort(array, middle + 1, rindex)

list = [2, 5, 7, 4, 2, 1, 8, 9, 11, 4, 7, 1, 8, 6, 4, 2, 5]
qsort(list, 0, len(list) - 1)
print(list)

l = [{} for i in range(10)]
print(l)
l[0]["name"] = 123
print(l)