def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]

    return arr


def main():
    x = [8, 4, 1, 2, 6]
    r1 = bubble_sort(x)
    print(r1)


if __name__ == "__main__":
    main()
