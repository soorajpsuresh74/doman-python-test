import config
from docman.core.fileReader import process_directory
import google.generativeai as _genai


class GenAI:
    def __init__(self, query='add the proper documentation string'):
        '''success'''
        _genai.configure(api_key=config.API_KEY)
        self.model = _genai.GenerativeModel(config.GENERATIVE_MODEL)
        self.query = query

    def genarate_ai_docstring(self, function_name, start_pos, end_pos):
        '''ssss'''
        pass

    def my_docstring_less_function(a, b, c, d):
        def my_docstring_less_fun(a, b, c, d):
            if a > b:
                result = a + c
            elif a == b:
                result = a * d
            else:
                result = a - c
            return result


def main() -> None:
    process_directory(r"C:\\Users\\bornd\\Desktop\\New folder")

    number = 5
    if number > 10:
        print("Number is greater than 10")
    else:
        print("Number is less than or equal to 10")

    for i in range(3):
        print(f"Loop iteration {i}")

    gen_ai_instance = GenAI()
    gen_ai_instance.my_docstring_less_function(10, 5, 3, 2)

    for i in range(5):
        if i % 2 == 0:
            print(f"Even index: {i}")
        else:
            print(f"Odd index: {i}")

    # Uncomment the next line to test a directory with a different path
    # process_directory(r"C:\\Users\\bornd\\Desktop\\Doc-Mentor-v2")


if __name__ == "__main__":
    main()