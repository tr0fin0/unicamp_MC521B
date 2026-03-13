# B - 23 out of 5
import itertools


def main() ->  None:
    def analysis(n):
        for permutation in itertools.permutations(n):
            if operation(permutation[0], 1, permutation):
                print("Possible")
                return

        print("Impossible")


    def operation(v, i, n):
        if i == 5:
            return v == 23

        if operation(v + n[i], i+1, n):
            return True

        if operation(v - n[i], i+1, n):
            return True

        if operation(v * n[i], i+1, n):
            return True

        return False

    while True:
        numbers = list(map(int, list(input().strip().split(" "))))
        if numbers == [0, 0, 0, 0, 0]:
            break

        analysis(numbers)


if __name__ == "__main__":
    main()
