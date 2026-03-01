# https://atcoder.jp/contests/abc258/tasks/abc258_c


def main():
    N, Q    = input().split(" ")
    S       = input()

    reference = 0
    for _ in range(int(Q)):
        type, x = input().split(" ")

        if (type == "1"):
            reference += int(x)

        if (type == "2"):
            print(S[(int(x) - reference) % len(S) - 1])

    return


if __name__ == "__main__":
    main()
