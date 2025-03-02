from core.queries import PYTHON_QUERY, PYTHON_CLASS_QUERY
from core.treeSitter.treeSitterLanguage import PYTHON_LANGUAGE, KOTLIN_LANGUAGE, JAVA_LANGUAGE, HTML_LANGUAGE


class PythonQuery:
    language = PYTHON_LANGUAGE
    function_query = language.query(PYTHON_QUERY)
    class_query = language.query(PYTHON_CLASS_QUERY)


class KotlinQuery:
    language = KOTLIN_LANGUAGE
    # query = language.query()


class JavaQuery:
    language = JAVA_LANGUAGE
    # query = language.query()


class HtmlQuery:
    language = HTML_LANGUAGE
    # query = language.query()


QUERY_CLASS_MAPPINGS = {
    '.py': PythonQuery(),
    # '.kt': KotlinQuery(),
    # '.java': JavaQuery(),
    # '.html': HtmlQuery(),
}
