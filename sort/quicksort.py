def quicksort(arr, low, high):
    if low >= high:
        return

    pivot_idx = partition(arr, low, high)
    quicksort(arr, low, pivot_idx - 1)
    quicksort(arr, pivot_idx + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]

    idx = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    idx += 1
    arr[high] = arr[idx]
    arr[idx] = pivot
    return idx


def main():
    arr = [55, 3, 7, 4, 69, 420, 42]
    print(quicksort(arr, 0, len(arr) - 1))


if __name__ == "__main__":
    main()
