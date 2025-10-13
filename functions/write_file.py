import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    if not os.path.abspath(path).startswith(os.path.abspath(working_directory)):
        return print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    #elif not os.path.exists(path):
        #os.makedirs(path)
    #    with open(path, "w") as f:
    #        f.write(content)
    else:
        with open(path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)