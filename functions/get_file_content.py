import os
from functions.config import *
from google import genai
from google.genai import types


def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    if not os.path.abspath(path).startswith(os.path.abspath(working_directory)):
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    elif not os.path.isfile(path):
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    else:
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
            return print(file_content_string)
        

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name, relative to the working directory.",
            ),
        },
    ),
)