# G - Vapor Pressure


def main() ->  None:
    a, b, c = input().strip().split(" ")
    A = int(a)
    B = int(b)
    C = int(c)

    while A > B * C:
        A -= 1

    print(A/B)

    return



if __name__ == "__main__":
    main()
