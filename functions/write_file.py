import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file= os.path.normpath(os.path.join(working_dir_abs, file_path))
        parent_dir = os.path.dirname(target_file)
    
        if os.path.isfile(target_file):
                valid_target_file= os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        else:
            raise Exception(f'Cannot write to "{file_path}" as it is a directory')
    
    
        if not valid_target_file:
            raise Exception(f'Cannot read "{file_path}" as it is outside the permitted working directory')
        else:
            os.makedirs(parent_dir,exist_ok=True)
            with open(target_file, "w") as f:
                f.write(content)
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            return content
            
    
    except Exception as e:
            print(f"Error: {e}")