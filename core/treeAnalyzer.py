from tree_sitter import Tree

from core.codeUpdater import code_updator
from core.docmanLogger.docmanLogger import setup_logger
from core.treeAnalyzerClasses.PyAnalyzer import PYAnalyzer

logger = setup_logger(name="tree analysis", log_file="logs/tree analysis.log")


async def analyse_tree(tree: Tree, query, code, language):
    root_node = tree.root_node
    if language == '.py':
        analyser = PYAnalyzer()
        logger.info("Starting the analysis process...")
        updated_function_details = await analyser.iterate_to_find_the_functions(root_node, query, code)
        new_code = code_updator(updated_function_details, code)
        logger.info("Analysis process complete.")
        print(new_code)

