# Funtion to read and write from txt files
def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)