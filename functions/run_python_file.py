import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file= os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        if os.path.isfile(target_file):
            valid_target_file= os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        else:
            raise Exception(f'"{file_path}" does not exist or is not a regular file')

        if not target_file.endswith(".py"):
             raise Exception(f'"{file_path}" is not a Python file')
        
        
        if not valid_target_file:
            raise Exception(f'Cannot execute "{file_path}" as it is outside the permitted working directory')
        else:
            command = ["python", target_file]
            if args:
                command.extend(args)
            py_process = subprocess.run(command, capture_output = True, timeout = 30, text = True)
            output = ""
        if py_process.check_returncode():
            code = py_process.returncode
            output += f"Process exited with code {code}"
        if py_process.stdout == None and py_process.stderr == None:
            output += "No output produced"
        return output + f"STDOUT: {py_process.stdout} STDERR: {py_process.stderr}"
           
        
    except Exception as e:
        print(f"Error: executing Python file: {e}")


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a subprocess in a file path relative to the working directory, providing output and process status",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to run the process from, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "description": "Additional arguments (optional)",
                },
            }
        },
    },
}