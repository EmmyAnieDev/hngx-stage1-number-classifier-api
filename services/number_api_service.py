import requests
from utils.number_properties import NumberProperties
from utils.constants import *
from collections import OrderedDict


class NumberAPIService:

    def __init__(self):
        self.number_properties = NumberProperties()

    def get_fun_fact(self, num):
        try:
            response = requests.get(f'{NUMBERS_API_BASE_URL}/{num}/math')
            if response.status_code == 200:
                return response.text
            return f"No fun fact available for number: {num}"
        except:
            return f"Could not fetch fun fact."

    def analyze_number(self, number):

        response_data = OrderedDict([
            ("number", number),
            ("is_prime", self.number_properties.is_prime(number)),
            ("is_perfect", self.number_properties.is_perfect(number)),
            ("properties", self.number_properties.get_properties(number)),
            ("digit_sum", self.number_properties.get_digit_sum(number)),
            ("fun_fact", self.get_fun_fact(number))
        ])

        return response_data