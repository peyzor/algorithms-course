# O(n) time complexity
def linear_search_index_of(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i

    return -1

def main():
    r1 = linear_search_index_of([1,4,2,5,78,3], 4)
    print(r1)

if __name__ == "__main__":
    main()
