# H - How many ways? 


def main() -> None:
    while True:
        N, X = map(int, input().split())
        if N == 0 and X == 0:
            break

        combinations = 0
        for i in range(1, N - 1):
            for j in range(i + 1, N):
                k = X - i - j
                if k > j and k <= N:
                    combinations += 1

        print(combinations)


if __name__ == "__main__":
    main()