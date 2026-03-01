# https://atcoder.jp/contests/abc267/tasks/abc267_b


def main():
    pins : str = input()

    columns = [
        int(int(pins[6]) > 0),
        int(int(pins[3]) > 0),
        int((int(pins[1]) + int(pins[7])) > 0),
        int((int(pins[0]) + int(pins[4])) > 0),
        int((int(pins[2]) + int(pins[8])) > 0),
        int(int(pins[5]) > 0),
        int(int(pins[9]) > 0)
    ]

    split = False
    if (int(pins[0]) == 0):
        for i in range(1, len(columns) - 1):
            if columns[i] == 0:
                
                if sum(columns[0 : i]) > 0 and sum(columns[i+1:]):
                    split = True

    print("Yes" if split else "No")

    return


if __name__ == "__main__":
    main()
