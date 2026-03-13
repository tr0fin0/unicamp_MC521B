# F - Don't Get Rooked



def main():
    empty   = '.'
    rook    = 'R'
    wall    = 'X'

    def safe(board, n, r, c):

        # upwards
        i = r - 1
        while i >= 0:
            if board[i][c] == wall:
                break

            if board[i][c] == rook:
                return False

            i -= 1


        # downwards
        i = r + 1
        while i < n:
            if board[i][c] == wall:
                break

            if board[i][c] == rook:
                return False

            i += 1


        # left
        j = c - 1
        while j >= 0:
            if board[r][j] == wall:
                break

            if board[r][j] == rook:
                return False

            j -= 1


        # right
        j = c + 1
        while j < n:
            if board[r][j] == wall:
                break

            if board[r][j] == rook:
                return False
            j += 1
        return True


    while True:
        n: int = int(input().strip())
        if n == 0:
            break

        board = [list(input().strip()) for _ in range(n)]

        best = 0
        def backtrack(position, rooks):
            nonlocal best
            if position == n * n:
                if rooks > best:
                    best = rooks

                return

            r = position // n
            c = position %  n

            if board[r][c] == empty and safe(board, n, r, c):
                board[r][c] = rook

                # trying positioning a rook
                backtrack(position + 1, rooks + 1)

                # posionting failed, fallback original empty configuration
                board[r][c] = empty

            backtrack(position + 1, rooks)


        backtrack(0, 0)
        print(best)


if __name__ == "__main__":
    main()
