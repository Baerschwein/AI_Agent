from functions.get_file_content import *

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result1 =get_file_content("calculator", "main.py")
print(result1)

result2= get_file_content("calculator", "pkg/calculator.py")
print(result2)

get_file_content("calculator", "/bin/cat")

get_file_content("calculator", "pkg/does_not_exist.py")
