
def merge_sort(arr, l, r):

    if l >= r:
        return

    mid = (l + r) // 2

    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)

    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


a = [2, 3, 1, 12, 2, 9, 5, 4]

merge_sort(a, 0, len(a) - 1)

print(a)
