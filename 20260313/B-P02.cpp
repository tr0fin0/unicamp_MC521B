// B - 23 out of 5
// Same behavior as Python function
#include <bits/stdc++.h>

bool operation(int v, int i, const std::vector<int> &n)
{
    if (i == 5)
        return v == 23;

    if (operation(v + n[i], i + 1, n))
        return true;

    if (operation(v - n[i], i + 1, n))
        return true;

    if (operation(v * n[i], i + 1, n))
        return true;

    return false;
}

void analysis(const std::vector<int> &nums)
{
    std::vector<int> p = nums;
    std::sort(p.begin(), p.end());

    do
    {
        if (operation(p[0], 1, p))
        {
            std::cout << "Possible\n";
            return;
        }
    } while (std::next_permutation(p.begin(), p.end()));

    std::cout << "Impossible\n";
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    while (true)
    {
        std::vector<int> numbers(5);
        for (int i = 0; i < 5; ++i)
        {
            if (!(std::cin >> numbers[i]))
            {
                return 0;
            }
        }

        if (numbers == std::vector<int>{0, 0, 0, 0, 0})
        {
            break;
        }

        analysis(numbers);
    }

    return 0;
}
