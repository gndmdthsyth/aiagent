import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)
    #print(os.path.abspath(path))
    if not os.path.abspath(path).startswith(os.path.abspath(working_directory)):
        return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(path):
        return print(f'Error: "{directory}" is not a directory')
    else:
        result = "Result for current directory:\n"
        contents = os.listdir(path)
        #print(contents)
        for item in contents:
            #print(item)
            item_path = os.path.abspath(os.path.join(path, item))
            size = os.path.getsize(item_path)
            result = result + f"- {item}: file_size={size} bytes, is_dir={os.path.isdir(item_path)}\n"



        return print(result)
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)