# https://atcoder.jp/contests/abc234/tasks/abc234_f


def main():
    def factorials(m, n):
        for i in range(1, n + 1):
            FACTORIALS[i] = FACTORIALS[i-1] * i % m


    def frequencies(string):
        f = {}
        for letter in string:
            f[letter] = f.get(letter, 0) + 1

        return f


    def permutation(letters):
        frequencies = list(letters.values())
        frequencies_sum = sum(frequencies)

        if frequencies_sum == 0:
            return 0

        den = 1
        for frequency in frequencies:
            den = den * FACTORIALS[frequency] % M

        num = FACTORIALS[frequencies_sum]
        return num * pow(den, M - 2, M) % M


    def permutations(letters):
        combinations = 0

        for letter in letters:
            if letters[letter] > 0:
                letters[letter] -= 1

                combinations += permutation(letters)
                combinations %= M

                combinations += permutations(letters)
                combinations %= M

                letters[letter] += 1

        return combinations


    S: str  = input()
    M: int  = 998244353
    N: int  = len(S)

    FACTORIALS          = [1] * (N + 1)
    factorials(M, N)


    print(permutations(frequencies(S)) % M)

    return


if __name__ == "__main__":
    main()
