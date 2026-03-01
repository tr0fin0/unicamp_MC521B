# https://atcoder.jp/contests/abc234/tasks/abc234_f


def main():
    S = input().strip()
    if not S:
        return

    M = 998244353
    N = len(S)

    FACTORIALS      = [1] * (N + 1)
    INV_FACTORIALS  = [1] * (N + 1)

    for i in range(1, N + 1):
        FACTORIALS[i] = (FACTORIALS[i - 1] * i) % M

    # Fermat's Little Theorem
    INV_FACTORIALS[N] = pow(FACTORIALS[N], M - 2, M)
    for i in range(N - 1, -1, -1):
        INV_FACTORIALS[i] = (INV_FACTORIALS[i + 1] * (i + 1)) % M


    def nCr(n, r):
        if r < 0 or r > n:
            return 0

        return FACTORIALS[n] * INV_FACTORIALS[r] % M * INV_FACTORIALS[n - r] % M


    frequencies = [0] * 26
    for char in S:
        frequencies[ord(char) - ord('a')] += 1


    # Dynamic Programming (DP)
    dp      = [0] * (N + 1)
    dp[0]   = 1 # base case

    current_length = 0

    for frequency in frequencies:
        if frequency == 0:
            continue

        next_dp = [0] * (N + 1) # new DP state

        # Iterate through all previously formed sequence lengths
        for j in range(current_length + 1):
            if dp[j] == 0:
                continue

            # We can pick 'k' instances of the current character (from 0 up to f)
            for k in range(frequency + 1):
                ways = (dp[j] * nCr(j + k, k)) % M
                next_dp[j + k] = (next_dp[j + k] + ways) % M

        dp = next_dp
        current_length += frequency


    print(sum(dp[1:]) % M)


if __name__ == "__main__":
    main()
