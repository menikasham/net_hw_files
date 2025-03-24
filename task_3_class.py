import os
import glob


class CheckFile:
    def __init__(self, directory='.'):
        self.directory = directory
        self.file_dict = {}

    def read_file(self, file):
        with open(file, encoding='utf8') as f:
            lines = f.readlines()
        return len(lines)

    def process_files(self):
        for file in glob.glob(f'{self.directory}/*.txt'):
            self.file_dict[os.path.basename(file)] = self.read_file(file)

    def write_file(self, output_file='result.txt'):
        sorted_dict = sorted(self.file_dict.items(), key=lambda x: x[1])
        for item in sorted_dict:
            with open(output_file, 'a', encoding='utf8') as f:
                with open(f'./{item[0]}', encoding='utf8') as F:
                    txt = F.readlines()
                    txt1 = ''.join(txt)
                    f.write(f'{item[0]}\n{item[1]}\n{txt1}\n')


if __name__ == '__main__':
    processor = CheckFile()
    processor.process_files()
    processor.write_file()
