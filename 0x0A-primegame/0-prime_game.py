#!/usr/bin/python3
"""Prime Game between Ben and Maria"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the
        maximum numbers in each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, returns None.
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """Generate a list of primes up to n."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
