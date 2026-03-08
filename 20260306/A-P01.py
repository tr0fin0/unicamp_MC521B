# https://www.acmicpc.net/problem/16692


def main() ->  None:
    N, C    = input().split(" ")
    T       = [ int(n) for n in input().split(" ") ]

    waiting     = T[:int(N)]
    sequence    = [ i for i in range(1, int(N)+1) ]
    for customer in T[int(N):]:
        v = min(waiting)
        i = waiting.index(v)

        sequence.append(i + 1)

        waiting = [ x - v for x in waiting ]
        waiting[i] = customer

    print(" ".join(str(x) for x in sequence))

    return



if __name__ == "__main__":
    main()
