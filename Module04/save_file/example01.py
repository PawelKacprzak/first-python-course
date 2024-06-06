# new_file = open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r')

# for line in new_file:
#     print(line, end = '')

# new_file.close()

with open('/Users/champa/Documents/Python/PythonDevCourse/Module04/save_file/example01.txt', 'r') as file:
    for line in file:
        print(line, end = '')
file.close()