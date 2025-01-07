# (class_definition
#         name: (identifier) @class_name
#         body: (block
#             (function_definition
#                 name: (identifier) @function_name
#                 body: (block
#                     (expression_statement
#                         (string) @class_docstring
#                     )?
#                 )
#             )*
#         ) @class_block
#     )
PYTHON_QUERY = """
(function_definition
    name: (identifier) @function_name
    parameters: (parameters) @parameters
    return_type: (type)? @return_type
    body: (block
        (expression_statement
            (string) @docstring)?
    ) @function_block)
"""
PYTHON_CLASS_QUERY = """
(class_definition
  name: (identifier) @class_name
  superclasses: (argument_list(attribute(identifier)@superclass))
  body: (block
          (expression_statement
              (string) @docstring)?
        ) @class_body
  )
"""
