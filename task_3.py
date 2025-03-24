import os
import glob


def read_file(filename):
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
    len_lines = len(lines)
    return len_lines


def write_result():
    file_dict = {}
    for file in glob.glob('./*.txt'):
        file_dict[os.path.basename(file)] = read_file(file)

    sorted_dict = sorted(file_dict.items(), key=lambda x: x[1])

    for item in sorted_dict:
        with open('./result.txt', 'a', encoding='utf8') as f:
            with open(f'./{item[0]}', encoding='utf8') as F:
                txt = F.readlines()
                txt1 = ''.join(txt)
                f.write(f'{item[0]}\n{item[1]}\n{txt1}\n')


write_result()
