import os
from functions.config import *
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file


call_names = {"get_files_info": get_files_info, "get_file_content": get_file_content,
                "run_python_file": run_python_file, "write_file": write_file
            }

def call_function(function_call_part, verbose=False):
    #print(function_call_part.name)
    if function_call_part.name not in call_names:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    func_args = {"working_directory": CWD}
    func_args.update(function_call_part.args)

    function_result = call_names[function_call_part.name](**func_args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
            )
        ],
    )