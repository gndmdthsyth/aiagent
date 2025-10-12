import os
import sys
from dotenv import load_dotenv
from functions.config import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file
    ]
)

def main():
    #print(sys.argv[1])
    if len(sys.argv) == 1:
        print("ERROR exiting.")
        sys.exit(1)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(tools = [available_functions],system_instruction=system_prompt
    ))
    #print(response.text)
    for call in response.function_calls:
        print(f"Calling function: {str(call.name)}({str(call.args)})")
    print(response.text)
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
