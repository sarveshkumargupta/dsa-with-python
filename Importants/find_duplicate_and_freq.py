
a = [2, 3, 1, 12, 2, 9, 5, 4, 9]

a.sort()  # Merge or any other sorting can be used instead

# Jump to next approach
count = 1
i = 0

while i < len(a):

    if i + 1 < len(a) and a[i] == a[i + 1]:
        count += 1
    else:
        print(f"Element -> {a[i]}, Count -> {count}")
        count = 1

    i += 1


# Two pointer approach
# i = 0
#
# while i < len(a):
#     j = i
#
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#
#     count = j - i
#     print(f"Element -> {a[i]}, Count -> {count}")
#
#     i = j


# dup_with_freq = {}
#
# for i in a:
#     if i in dup_with_freq:
#         dup_with_freq[i] += 1
#     else:
#         dup_with_freq[i] = 1
#
#
# print(dup_with_freq)



