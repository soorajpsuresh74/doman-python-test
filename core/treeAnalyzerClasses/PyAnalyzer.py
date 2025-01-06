import re
from core.docmanLogger.docmanLogger import setup_logger
from core.generator.docstringGenarator import docstring_generator_function_for_python

logger = setup_logger(name="py analyzer", log_file="logs/py analyzer.log")


class PYAnalyzer:

    @staticmethod
    async def iterate_to_find_the_functions(root_node, query, code):
        payload = code
        updated_function_details = []

        try:
            for match_tuple in query.matches(root_node):
                node_dict = match_tuple[1]

                function_name_node = node_dict.get('function_name', [None])[0]
                parameters_node = node_dict.get('parameters', [None])[0]
                return_type_node = node_dict.get('return_type', [None])[0]
                docstring_node = node_dict.get('docstring', [None])[0]
                function_block_node = node_dict.get('function_block', [None])[0]

                func_name_text = function_name_node.text.decode('utf-8') if function_name_node else "Unknown"
                return_type_text = return_type_node.text.decode('utf-8') if return_type_node else None
                parameters_text = parameters_node.text.decode('utf-8') if parameters_node else "()"
                docstring_text = docstring_node.text.decode('utf-8') if docstring_node else None
                function_text = function_block_node.text.decode('utf-8') if function_block_node else None

                if function_block_node:
                    function_details = {
                        "function_name": func_name_text,
                        "parameters": parameters_text,
                        "return_type": return_type_text,
                        "function_docstring": docstring_text,
                        "function_body": function_text
                    }

                    if not docstring_text:

                        generated_docstring = await docstring_generator_function_for_python(function_details)

                        if generated_docstring:
                            function_start = function_block_node.start_byte
                            function_end = function_block_node.end_byte
                            full_function_code = payload[function_start:function_end]
                            updated_function_details.append({
                                "function_name": func_name_text,
                                "parameters": parameters_text,
                                "return_type": return_type_text,
                                "function_docstring": generated_docstring,
                                "function_body": full_function_code,
                            })
                        else:
                            logger.warning(f"Failed to generate docstring for {func_name_text}")
                    updated_function_details.append(function_details)
            logger.info(updated_function_details)
            return updated_function_details

        except Exception as e:
            logger.error(f"Exception occurred while iterate_to_find_the_functions : {e}")
            return []

