def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as flow:
        result = flow.read()
        return result

def writing_file(user_string: str, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as flow:
        flow.writelines(user_string)