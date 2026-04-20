
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

t = 12


def binary_search(arr):
    i = 0
    j = len(arr)

    while i <= j:
        mid = (i + j) // 2

        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            i = mid + 1
        else:
            j = mid - 1


print(binary_search(arr))
