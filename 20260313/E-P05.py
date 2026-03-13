# E - Precondition


def main() ->  None:
    S: str = input().strip()
    T: str = input().strip()

    valid: bool = True
    for i, c in enumerate(S):
        if i == 0:
            continue

        if (c == c.upper() and S[i-1] not in T):
            valid = False
            break

    print("Yes" if valid else "No")

    return



if __name__ == "__main__":
    main()
