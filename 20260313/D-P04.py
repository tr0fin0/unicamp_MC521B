# D - You're Given a String...


def main():
    S: str = input().strip()
    N: int = len(S)

    occurrences = {}
    longest = 0
    for l in range(N - 1, 0, -1):
        for i in range(N - l + 1):
            sub = S[i:i+l]

            occurrences[sub] = occurrences.get(sub, 0) + 1
            if occurrences[sub] > 1 and len(sub) > longest:
                longest = len(sub)

    print(longest)


if __name__ == "__main__":
    main()