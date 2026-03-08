# B - Grid

def main() ->  None:
    N: int = int(input())

    while N != 0:
        """
        N:      number of rows
        N:      number of columns
        2N-1:   number of diagonals in north-east to south-west direction
        2N-1:   number of diagonals in north-west to south-east direction
        """
        sequences       = [0] * (6*N - 2)
        max_sequence    = 0

        grid = [
            list(map(int, list(input()))) for _ in range(N)
        ]


        for i in range(N):
            for j in range(N):
                row = 0*N + i
                col = 1*N + j
                dnw = 3*N - 1 + (i - j)
                dne = 4*N - 1 + (i + j)

                if grid[i][j] == 1:
                    for pos in [row, col, dnw, dne]:
                        sequences[pos] += 1
                        if sequences[pos] > max_sequence:
                            max_sequence = sequences[pos]

                else:
                    for pos in [row, col, dnw, dne]:
                        sequences[pos] = 0


        print(max_sequence)
        N = int(input())


    return



if __name__ == "__main__":
    main()
