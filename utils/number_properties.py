import math


class NumberProperties:

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect(num):
        if num <= 1:
            return False
        sum_factors = sum(i for i in range(1, num) if num % i == 0)
        return sum_factors == num

    @staticmethod
    def is_armstrong(num):
        if num < 0:
            return False
        num_str = str(num)
        power = len(num_str)
        total = sum(int(digit) ** power for digit in num_str)
        return total == num

    @staticmethod
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    @staticmethod
    def get_properties(num):
        properties = []

        if NumberProperties.is_armstrong(num):
            properties.append("armstrong")

        properties.append("even" if num % 2 == 0 else "odd")

        return properties