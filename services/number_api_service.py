import requests
from utils.number_properties import NumberProperties
from utils.constants import *
from concurrent.futures import ThreadPoolExecutor


class NumberAPIService:

    def __init__(self):
        self.number_properties = NumberProperties()

    def get_fun_fact(self, num):
        try:
            response = requests.get(f'{NUMBERS_API_BASE_URL}/{num}/math', timeout=0.3)
            if response.status_code == 200:
                return response.text
            return f"No fun fact available for number: {num}"
        except:
            return f"Could not fetch fun fact."

    def analyze_number(self, number):
        with ThreadPoolExecutor() as executor:
            fun_fact_future = executor.submit(self.get_fun_fact, number)
            is_prime_future = executor.submit(self.number_properties.is_prime, number)
            is_perfect_future = executor.submit(self.number_properties.is_perfect, number)
            properties_future = executor.submit(self.number_properties.get_properties, number)
            digit_sum_future = executor.submit(self.number_properties.get_digit_sum, number)

            response_data = {
                "number": number,
                "is_prime": is_prime_future.result(),
                "is_perfect": is_perfect_future.result(),
                "properties": properties_future.result(),
                "digit_sum": digit_sum_future.result(),
                "fun_fact": fun_fact_future.result()
            }
        return response_data