import re
import time

from core.docmanLogger.docmanLogger import setup_logger
from core.generator.docstringGenarator import docstring_generator_function_for_python, \
    docstring_generator_class_function_for_python
from typing import Any, Dict, List, Optional

# Initialize logger
logger = setup_logger(name="py analyzer", log_file="logs/py analyzer.log")


class PYAnalyzer:

    @staticmethod
    def decode_node_text(node: Optional[Any]) -> Optional[str]:
        """Decode the text of a node if it exists."""
        return node.text.decode('utf-8') if node else None

    @staticmethod
    async def iterate_to_find_the_functions(
        root_node: Any, function_query: Any
    ) -> List[Dict[str, Any]]:
        """
        Iterates through a tree to find functions and their details.

        Args:
            root_node (Any): The root node of the syntax tree.
            query (Any): A query object to match nodes in the syntax tree.
            code (str): The source code as a string.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing function details.
        """
        updated_function_details = []

        try:
            # Iterate through the query matches
            for match_tuple in function_query.matches(root_node):
                node_dict = match_tuple[1]

                # Extract nodes
                function_name_node = node_dict.get('function_name', [None])[0]
                parameters_node = node_dict.get('parameters', [None])[0]
                return_type_node = node_dict.get('return_type', [None])[0]
                docstring_node = node_dict.get('docstring', [None])[0]
                function_block_node = node_dict.get('function_block', [None])[0]

                # Decode node text
                func_name_text = PYAnalyzer.decode_node_text(function_name_node) or "Unknown"
                return_type_text = PYAnalyzer.decode_node_text(return_type_node)
                parameters_text = PYAnalyzer.decode_node_text(parameters_node) or "()"
                docstring_text = PYAnalyzer.decode_node_text(docstring_node)
                function_text = PYAnalyzer.decode_node_text(function_block_node)

                # Construct function details
                function_details = {
                    "function_name": func_name_text,
                    "parameters": parameters_text,
                    "return_type": return_type_text,
                    "function_docstring": None,
                    "function_body": function_text,
                }

                # Handle missing docstrings
                if not docstring_text:
                    # added delay for managing the google genartive api response
                    time.sleep(0.4)
                    generated_docstring = await docstring_generator_function_for_python(function_details)
                    if generated_docstring:
                        logger.info(f"Generated docstring for {func_name_text}")
                        function_details["function_docstring"] = generated_docstring
                    else:
                        logger.warning(f"Failed to generate docstring for {func_name_text}")

                # Add to the updated function details list only once
                updated_function_details.append(function_details)

            logger.info("Function details updated successfully.")
            return updated_function_details

        except Exception as e:
            logger.error(f"Exception occurred in iterate_to_find_the_functions: {e}")
            return []

    @staticmethod
    async def iterate_over_code_to_find_classes(root_node: Any, class_query: Any) -> List[Dict[str, Any]]:
        updated_class_details = []
        try:

            for match_tuple in class_query.matches(root_node):
                node_dict = match_tuple[1]

                # Extract nodes
                class_name_node = node_dict.get('class_name', [None])[0]
                superclasses_node = node_dict.get('superclass', [None])[0]
                docstring_node = node_dict.get('docstring', [None])[0]
                class_block_node = node_dict.get('class_body', [None])[0]

                class_name_text = PYAnalyzer.decode_node_text(class_name_node) or "Unknown"
                superclasses_text = PYAnalyzer.decode_node_text(superclasses_node)
                docstring_text = PYAnalyzer.decode_node_text(docstring_node)
                class_block_text = PYAnalyzer.decode_node_text(class_block_node)

                class_details = {
                    "class_name": class_name_text,
                    "super_classes": superclasses_text,
                    "class_docstring": None,
                    "class_body": class_block_text,
                }

                if not docstring_text:
                    # added delay for managing the google genartive api response
                    time.sleep(0.4)
                    generated_docstring = await docstring_generator_class_function_for_python(class_details)
                    if generated_docstring:
                        logger.info(f"Generated docstring for {class_name_text}")
                        class_details["class_docstring"] = generated_docstring
                    else:
                        logger.warning(f"Failed to generate docstring for {class_name_text}")

                updated_class_details.append(class_details)

            logger.info("class details updated successfully.")
            return updated_class_details

        except Exception as e:
            logger.error(f"Exception occurred in iterate_over_code_to_find_classes: {e}")
            return []



