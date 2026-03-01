# https://dmoj.ca/problem/ccc14j3


def main():
    n : str = input()

    score = [100, 100]

    for _ in range(int(n)):
        play = input().split(' ')

        if int(play[0]) > int(play[1]):
            score[1] -= int(play[0])

        if int(play[1]) > int(play[0]):
            score[0] -= int(play[1])

    print(f"{score[0]}\n{score[1]}")

    return



if __name__ == "__main__":
    main()
