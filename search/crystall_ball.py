import math


def crystall_balls(breaks: list[bool]) -> int:
    jump_amount = math.floor(math.sqrt(len(breaks)))

    i = jump_amount
    while i < len(breaks):
        if breaks[i]:
            break

        i += jump_amount

    i -= jump_amount

    j = 0
    while j <= jump_amount and i < len(breaks):
        if breaks[i]:
            return i - 1

        j += 1
        i += 1

    return -1


def main():
    breaks = [False for _ in range(60)]
    for _ in range(40):
        breaks.append(True)

    r1 = crystall_balls(breaks)
    print(r1)


if __name__ == "__main__":
    main()
