import re

from core.docmanLogger.docmanLogger import setup_logger

logger = setup_logger(name="code updator", log_file="logs/code updator.log")


def code_updator(updated_function_details: list, payload: str):
    code = payload
    for func_detail in updated_function_details:
        func_name = func_detail['function_name']
        docstring = func_detail.get('function_docstring')

        if not docstring:
            logger.warning(f"Docstring not found for function {func_name}. Skipping update.")
            continue

        pattern = rf"^([ \t]*)def {func_name}\((.*?)\)(?:\s*->\s*\w+)?:"
        matches = list(re.finditer(pattern, code, re.MULTILINE))

        for match in matches:
            indentation = match.group(1)
            func_signature = match.group(0)

            docstring_indentation = indentation + "    "
            formatted_docstring = (
                f'{docstring_indentation}"""\n'
                f'{docstring_indentation}{docstring.replace("\n", f"\n{docstring_indentation}")}\n'
                f'{docstring_indentation}"""'
            )

            replacement = f"{func_signature}\n{formatted_docstring}"
            code = code[:match.start()] + replacement + code[match.end():]
    logger.info(code)
    return code
