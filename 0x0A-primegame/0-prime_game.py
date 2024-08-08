#!/usr/bin/python3
"""Task 0. Prime Game module: Maria and Ben
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    max_round = max(nums)

    is_prime = [True] * (max_round + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_round**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_round + 1, i):
                is_prime[j] = False

    maria_wins, ben_wins = 0, 0

    for round_limit in nums:
        prime_total = sum(is_prime[2:round_limit + 1])
        if prime_total % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
