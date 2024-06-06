# with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example02.txt', 'r') as file:
#     line = file.readline()
#     print(line)

# with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines, end = '')

# with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end = '')

# with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r') as file:
#     line = file.readline()
#     while line:
#         print(line, end = '')
#         line = file.readline()

with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r') as file:
    lines = file.read()
    print(lines)
