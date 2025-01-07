from traceback import print_tb

from dotenv import load_dotenv
import os

load_dotenv()

class ExampleClass:
    def __init__(self):
        self.api_key = os.getenv("TEST_KEY")
        if not self.api_key:
            raise ValueError("TEST_KEY is not configured in the environment")

test_object = ExampleClass()

print(test_object.api_key)








