#!/usr/bin/python3
"""
They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who
the winner of each game is.
"""


def generate_primes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


def calculate_winner(n):
    """Calculate the winner for a single game with n elements."""
    primes = generate_primes(n)

    if not primes or primes[-1] > n:
        return "Ben"

    # Count the number of prime removal turns
    turns = len([p for p in primes if p <= n])

    # If the number of turns is odd, Maria wins; otherwise, Ben wins
    return "Maria" if turns % 2 == 1 else "Ben"


def isWinner(x, nums):
    """Determine the overall winner of x games."""
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
