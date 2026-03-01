# https://atcoder.jp/contests/abc124/tasks/abc124_a


def main():
    buttons : str = input()

    button_A = int(buttons.split(" ")[0])
    button_B = int(buttons.split(" ")[1])

    total = 0
    total += max(button_A, button_B)

    if (button_A > button_B):
        button_A -= 1

    if (button_B > button_A):
        button_B -= 1

    total += max(button_A, button_B)

    print(total)

    return


if __name__ == "__main__":
    main()
