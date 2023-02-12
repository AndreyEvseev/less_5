import random
from Func_files import read_file as rf, writing_file as wf

def data_flow_generator(user_file):
    number_characters = random.randint(5, 20)
    simbol_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data_flow = ''
    for i in range(number_characters):
        simbol_flow = random.choice(simbol_str)
        number_repetitions = random.randint(1, 50)
        for j in range(number_repetitions):
            data_flow += simbol_flow
    wf(data_flow, user_file)
    return data_flow

def rle_encoding(data):
    encode_rle = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode_rle += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode_rle += str(count) + prev_char
    return encode_rle

def rle_decoding(data):
    decode_rle = ''
    count = ''
    for char in data:
        if char in data:
            if char.isdigit():
                count +=char
            else:
                decode_rle += char * int(count)
                count = ''
    return decode_rle

input_file = 'files_task4/input_data.txt'
comprssed_file = 'files_task4/compressed_data.txt'
recovered_file = 'files_task4/recovered_data.txt'

way = input('Если Вы хотите сгенерировать новый поток данных, введите 1,\n'
    'если нет - введите любое другое число: ')
if way == '1':
    data_flow_generator(input_file)

incoming_stream = rf(input_file)
compressed_data = rle_encoding(incoming_stream)
wf(compressed_data, comprssed_file)
restored_data = rle_decoding(compressed_data)
wf(restored_data, recovered_file)
