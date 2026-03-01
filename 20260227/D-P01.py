# https://atcoder.jp/contests/abc260/tasks/abc260_b


def main():
    N, X, Y, Z  = input().split(" ")
    mathematics = list(map(int, input().split()))
    english     = list(map(int, input().split()))


    indexes = []
    for _ in range(int(X)):
        index = mathematics.index(max(mathematics))

        if (index not in indexes):
            indexes.append(index)
            mathematics[index]  = -1
            english[index]      = -1

    for _ in range(int(Y)):
        index = english.index(max(english))

        if (index not in indexes):
            indexes.append(index)
            mathematics[index]  = -1
            english[index]      = -1

    accumulated = [int(x) + int(y) for x, y in zip(mathematics, english)]
    for _ in range(int(Z)):
        index = accumulated.index(max(accumulated))

        if (index not in indexes):
            indexes.append(index)
            accumulated[index]  = -1


    for index in sorted(indexes):
        print(index + 1)

    return


if __name__ == "__main__":
    main()
