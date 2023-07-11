# a heap is self-balancing, can be used for priority
import math


class MinHeap:
    def __init__(self):
        self.length = 0
        self.data = []

    def heapify_up(self, idx):
        if idx == 0:
            return

        parent_idx = self.parent(idx)
        parent_value = self.data[parent_idx]
        value = self.data[idx]

        if parent_value > value:
            self.data[idx] = parent_value
            self.data[parent_idx] = value
            self.heapify_up(parent_idx)

    def heapify_down(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        if idx >= self.length - 1 or left_idx >= self.length - 1:
            return

        value = self.data[idx]
        left_value, right_value = self.data[left_idx], self.data[right_idx]

        # swap the value with the smallest of children
        if left_value > right_value and value > right_value:
            self.data[idx] = right_value
            self.data[right_idx] = value
            self.heapify_down(right_idx)

        elif left_value < right_value < value:
            self.data[idx] = left_value
            self.data[left_idx] = value
            self.heapify_down(right_idx)

    def insert(self, value):
        self.data.append(value)
        self.heapify_up(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            return

        out = self.data[0]
        if self.length == 1:
            self.data = []
            self.length -= 1
            return out

        self.data[0] = self.data[self.length - 1]
        self.data.pop()
        self.length -= 1
        self.heapify_down(0)
        return out

    def parent(self, idx):
        return math.floor((idx - 1) / 2)

    def left_child(self, idx):
        return 2 * idx + 1

    def right_child(self, idx):
        return 2 * idx + 2


def main():
    mh = MinHeap()
    mh.insert(70)
    mh.insert(80)
    mh.insert(100)
    mh.insert(200)
    mh.insert(50)
    mh.insert(30)
    mh.insert(7)

    print("data", mh.data)
    print("length", mh.length)
    print("delete", mh.delete())
    print("length", mh.length)
    print("data", mh.data)
    print("delete", mh.delete())
    print("length", mh.length)
    print("data", mh.data)
    print("delete", mh.delete())
    print("delete", mh.delete())
    print("delete", mh.delete())
    print("delete", mh.delete())
    print("delete", mh.delete())
    print("length", mh.length)
    print("data", mh.data)


if __name__ == "__main__":
    main()
