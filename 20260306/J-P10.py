# https://codeforces.com/problemset/problem/438/D


def main() ->  None:
    N, M    = input().split(" ")
    A       = list(map(int, input().split(" ")))

    for _ in range(int(M)):
        operation = input().split(" ")

        match int(operation[0]):
            case 1:
                _, l, r = operation
                print(f"{sum(A[int(l)-1 : int(r)])}")

            case 2:
                _, l, r, x = operation
                
                for i in range(int(l)-1, int(r)):
                    A[i] = int(A[i]) % int(x)

            case 3:
                _, k, x = operation
                A[int(k)-1] = int(x)

    return



if __name__ == "__main__":
    main()
