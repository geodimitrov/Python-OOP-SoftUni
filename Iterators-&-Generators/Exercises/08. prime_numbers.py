def get_primes(nums):

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    for num in nums:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))