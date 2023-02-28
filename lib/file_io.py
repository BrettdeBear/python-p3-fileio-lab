def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as temp:
        temp.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as temp:
        temp.write(append_content)

def read_file(file_name):
    text_file = open(f'{file_name}.txt')
    return text_file.read()
