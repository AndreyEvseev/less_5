from Func_files import read_file as rf, writing_file as wf

def func_transfrom_text(simbols: list, source_text: str) -> list:
    transfrom_text = source_text
    transfrom_text = transfrom_text.replace('\n', '\\n ')
    for item in range(len(simbols)):
        transfrom_text = transfrom_text.replace(simbols[item], ' ' + simbols[item]) 
    while transfrom_text.count('  ') != 0:
        transfrom_text = transfrom_text.replace('  ', ' ')
    transfrom_text = transfrom_text.split()
    return transfrom_text

def func_exclude_text(exclude_str: str, option: str, transfrom_text: list) -> list:
    exclude_list = transfrom_text
    for el in transfrom_text:
        if option == '1':
            if exclude_str.lower() in el.lower():
                exclude_list.remove(el) 
        else:
            if exclude_str in el:
                exclude_list.remove(el) 
    return exclude_list

def recovery_exclude_text(exclude_list: list, simbols: list) -> str:
    exclude_text = " ".join(exclude_list)
    simbols2 = [' ' + item for item in simbols]
    for item in range(len(simbols2)):
        exclude_text = exclude_text.replace(simbols2[item], simbols[item]) 
    exclude_text = exclude_text.replace('\\n ', '\n')
    return exclude_text

exclude_str = 'абв'
simbols = ['.', ',', ':', ';', '!', '?', '\\n']
work_file = 'files_task1/text_course.txt'
source_text = rf(work_file)
option = input('Если слова нужно удалить без учёта регистра, введите 1.\n'
    'Если нужно учитывать регистр, введите любой другой символ: ')
transfrom_text = func_transfrom_text(simbols, source_text)
exclude_list = func_exclude_text(exclude_str, option, transfrom_text)
exclude_text = recovery_exclude_text(exclude_list, simbols)
if option == '1':
    option = 'без учёта регистра'
else:
    option = 'с учётом регистра'
print(f'\nРезультатом удаления из исходного текста:\n"{source_text}"\n'
    f'слов, содержащих группу символов "{exclude_str}" {option}, является новый '
        f'текст: \n"{exclude_text}".' )

if input('Для записи нового текста в файл нажмите "1": ') == '1':
    exclude_file = 'files_task1/text_exclude.txt'
    wf(exclude_text, exclude_file)
