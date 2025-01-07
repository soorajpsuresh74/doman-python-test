import os
import shutil

from tree_sitter import Tree

from core.docmanLogger.docmanLogger import setup_logger
from core.treeAnalyzer import analyse_tree
from core.treeSitter.treeSitterConfig import LANGUAGE_PARSERS
from core.treeSitter.treeSitterQueryClasses import QUERY_CLASS_MAPPINGS

logger = setup_logger(name="docman", log_file="logs/docman.log")


def detect_language_parser_queries(file_path):
    _, ext = os.path.splitext(file_path)
    return LANGUAGE_PARSERS.get(ext.lower()), QUERY_CLASS_MAPPINGS.get(ext.lower()), ext.lower()


def make_syntax_tree(code: str, language_parser) -> Tree:
    return language_parser(code)


class Docman:
    def __init__(self, directory: str, parent_directory: str) -> None:
        self.directory = directory
        self.project_name = os.path.basename(os.path.normpath(directory))
        self.target_directory = os.path.join(parent_directory, self.project_name)

        if not os.path.exists(self.target_directory):
            os.makedirs(self.target_directory)

    async def process_directory(self) -> None:
        if not os.path.exists(self.directory):
            logger.error(f"Directory does not exist: {self.directory}")
            raise Exception(f"Directory does not exist: {self.directory}")

        logger.info(f"Processing directory: {self.directory}")

        for root, dirs, files in os.walk(self.directory):
            # Compute relative path to replicate the directory structure
            relative_path = os.path.relpath(root, self.directory)
            target_root = os.path.join(self.target_directory, relative_path)

            if not os.path.exists(target_root):
                os.makedirs(target_root)

            for file_name in files:
                file_path = os.path.join(root, file_name)
                language_parser, query, language = detect_language_parser_queries(file_path)

                if language_parser and query:
                    try:
                        logger.info(f"Processing file: {file_path}")
                        with open(file_path, 'r', encoding="utf-8") as file:
                            code = file.read()

                            tree = make_syntax_tree(code, language_parser)

                            updated_code = await analyse_tree(tree, query, code, language)

                            target_file_path = os.path.join(target_root, file_name)
                            with open(target_file_path, 'w', encoding="utf-8") as target_file:
                                target_file.write(updated_code)

                            logger.info(f"Successfully processed file: {file_path}")
                    except Exception as e:
                        logger.error(f"An exception occurred while processing {file_path}: {e}")
                        print(f"An exception occurred in the process directory function as {e}")
                else:
                    # Copy non-Python files to the target directory
                    try:
                        target_file_path = os.path.join(target_root, file_name)
                        shutil.copy2(file_path, target_file_path)
                        logger.info(f"Copied non-Python file to {target_file_path}")
                    except Exception as e:
                        logger.error(f"Failed to copy file {file_path} to {target_file_path}: {e}")
