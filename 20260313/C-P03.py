# C - Sumsets


def main():
    while True:
        n: int = int(input().strip())
        if n == 0:
            break

        numbers = [int(input().strip()) for _ in range(n)]
        numbers.sort()


        sums = {}
        for i in range(n):
            number = numbers[i]

            for j in range(i + 1, n):
                s = number + numbers[j]
                if s in sums:
                    sums[s].append((i, j))
                else:
                    sums[s] = [(i, j)]

        solution = False
        for index_d in range(n - 1, -1, -1):
            value_d = numbers[index_d]

            for index_c in range(n):
                if index_c == index_d:
                    continue
                value_c = numbers[index_c]

                diff = value_d - value_c
                if diff not in sums:
                    continue

                for index_a, index_b in sums[diff]:
                    if (
                        index_a != index_d and
                        index_a != index_c and
                        index_b != index_d and
                        index_b != index_c
                    ):
                        solution = True
                        print(value_d)

                        break

                if solution:
                    break

            if solution:
                break

        if not solution:
            print("no solution")


if __name__ == "__main__":
    main()
