# A - Replace


def main() -> None:
    N: int  = int(input().strip())
    S: list = list(input().strip())

    patterns = {
        "axa",
        "exe",
        "ixi",
        "oxo",
        "uxu"
    }

    for i in range(N - 2):
        if "".join(S[i:i+3]) in patterns:
            S[i] = S[i+1] = S[i+2] = "."

    print("".join(S))


if __name__ == "__main__":
    main()
