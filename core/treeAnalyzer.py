from tree_sitter import Tree

from core.codeUpdater import function_code_updator_with_docstring, class_code_updator_with_docstring
from core.docmanLogger.docmanLogger import setup_logger
from core.treeAnalyzerClasses.PyAnalyzer import PYAnalyzer

logger = setup_logger(name="tree analysis", log_file="logs/tree analysis.log")


async def analyse_tree(tree: Tree, query, code, language):
    function_query = query.function_query
    class_query = query.class_query
    root_node = tree.root_node
    if language == '.py':
        analyser = PYAnalyzer()
        logger.info("Starting the analysis process...")

        updated_function_details = await analyser.iterate_to_find_the_functions(root_node=root_node, function_query=function_query)
        functional_analysis_output = function_code_updator_with_docstring(updated_function_details, code)
        updated_class_details = await analyser.iterate_over_code_to_find_classes(root_node=root_node, class_query=class_query)
        class_analysis_output = class_code_updator_with_docstring(updated_class_details, functional_analysis_output)

        logger.info("Analysis process complete.")
        print(class_analysis_output)
        return class_analysis_output

