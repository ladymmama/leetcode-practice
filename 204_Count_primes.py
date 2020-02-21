class Solution:
    """
    @param n: a integer
    @return: return a integer
    """

    def countPrimes(self, n):
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        # sieve method
        if n <= 2:
            return 0

        count = 0
        is_prime = [1] * n  # create a from 0 to n-1, every item in this list is 1
        is_prime[0] = False  # index 0 and 1 becomes 0
        is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):  # for every number from 2 to squareroot n
            if is_prime[i]:  # if we find a prime x
                is_prime[i * i: n: i] = [False] * len(
                    is_prime[i * i: n: i])  # we mark every  x' multiple as false that start from x^2 to n,

        return sum(is_prime)  # count = the total number of 1 in this list