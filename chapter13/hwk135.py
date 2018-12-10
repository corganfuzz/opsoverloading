
filename = input("Enter a filename: ")
old_string = input("Enter the old string to be replaced: ")
new_string = input("Enter the new string to replace the old string: ")
with open(filename, 'r') as file:
    fileData = file.read()

fileData = fileData.replace(old_string, new_string)

with open(filename, 'w') as file:
    file.write(fileData)
