from core.docmanLogger.docmanLogger import setup_logger
import re

import google.generativeai as _genai
from config import KEY

_genai.configure(api_key=KEY)
model = _genai.GenerativeModel('gemini-1.5-flash')

logger = setup_logger(name="docstring generator", log_file="logs/docstring generator.log")


async def docstring_generator_function_for_python(function_dict):
    try:
        prompt = f"""
        Function Name: {function_dict.get('function_name')}
        Parameters: {function_dict.get('parameters')}
        Return Type: {function_dict.get('return_type')}
        Function Body:
        {function_dict.get('body')}
        Please generate a docstring for the above function."""
        logger.info(prompt)

        response = model.generate_content(prompt)
        logger.info(response)

        if response and response.candidates:
            docstring = response.candidates[0].content.parts[0].text
            match = re.search(r'"""(.*?)"""', docstring, re.DOTALL)

            if match:
                generated_docstring = match.group(1).strip()
                logger.info(generated_docstring)
                return generated_docstring
            else:
                logger.error("no match in docstring_generator_function_for_python")
                return None
        else:
            return None

    except Exception as e:
        print(f"Exception occurred {e}")
        logger.error("try-catch fail in docstring_generator_function_for_python")
        return None
