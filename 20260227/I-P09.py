# https://dmoj.ca/problem/ccc16s1


def main():
    def letters(s):
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        return d

    word_1 = letters(input())
    word_2 = letters(input())

    wildcard_anagram = True
    for k, v in word_1.items():
        if (word_2.get(k, 0) > v):
            wildcard_anagram = False
            break

        if (word_2.get(k, 0) < v):
            if (word_2.get(k, 0) + word_2.get("*", 0) >= v):
                word_2["*"] -=  v - word_2.get(k, 0)

            else:
                wildcard_anagram = False
                break

    print("A" if wildcard_anagram else "N")

    return


if __name__ == "__main__":
    main()
