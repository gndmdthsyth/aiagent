import os
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    path = os.path.join(working_directory, file_path)
    if not os.path.abspath(path).startswith(os.path.abspath(working_directory)):
        return print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    elif not os.path.isfile(path):
        #print(path)
        return print(f'Error: File "{file_path}" not found.')
    
    elif not path.endswith(".py"):
        return print(f'Error: "{file_path}" is not a Python file.')
    
    else:
        run_path = ["python", path, *args]
        result = subprocess.run(run_path, capture_output=True, timeout=30, text=True)
        if not result.stdout:
            return print("No output produced")
        elif result.returncode != 0:
            return print(f"STDOUT: {result.stdout}STDERR: {result.stderr} Process exited with code {result.returncode}")
        
        return print(f"STDOUT: {result.stdout}STDERR: {result.stderr}")
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to run.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional arguments to run the file.",
            ),
        },
    ),
)