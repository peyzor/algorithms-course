# O(n) time complexity
def linear_search_index_of(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i

    return -1

# always ask yourself is my dataset ordered, because if it is we can apply some optimization
def binary_search_index_of(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_index_of_rec(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    mid_value = arr[mid]

    if mid_value == target:
        return mid
    elif mid_value < target:
        return binary_search_index_of_rec(arr, target, mid + 1, high)
    else:
        return binary_search_index_of_rec(arr, target, low, mid - 1)


def main():
    r1 = linear_search_index_of([1, 4, 2, 5, 78, 3], 4)
    print(r1)
    x = [1, 2, 3, 4, 5, 78]
    r2 = binary_search_index_of(x, 4)
    print(r2)
    r3 = binary_search_index_of_rec(x, 4, 0, len(x) - 1)
    print(r3)


if __name__ == "__main__":
    main()
