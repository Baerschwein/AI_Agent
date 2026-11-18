import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        if os.path.isdir(target_dir):
             valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        else:
            raise Exception(f'"{directory}" is not a directory')

            

        if not valid_target_dir:
            raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')
        else: 
            #return print(f'Success: "{directory}" is within the working directory')
        
            items= os.listdir(target_dir)
            for item in items:
                abs_item= os.path.join(target_dir, item)
                size = os.path.getsize(abs_item)
                is_dir = os.path.isdir(abs_item)
                print(f"{item}: file_size={size}, is_dir={is_dir}")

    except Exception as e:
         print(f"Error: {e}")
