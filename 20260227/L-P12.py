# https://atcoder.jp/contests/abc234/tasks/abc234_f


def main():
    def factorial(n, r = 0):
        if n==0:
            return 1

        fact = 1
        for i in range(1, n - r + 1):
            fact *= i

        return fact

    def letters(s):
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1

        return d

    S: str = input()


    word = letters(S)
    size = len(word)
    print(f"word\t{word}")
    print(f"size\t{size}")

    permutations = 0
    for i in range(1, size + 2):
        print(f"i\t{i}")
        permutations += factorial(size)


    print(permutations % 998244353)
    return


if __name__ == "__main__":
    main()
