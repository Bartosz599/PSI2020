# plik file_manager
##
## 8 ##
##
class FileManager():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        uchwyt = open('plik.txt')
        dane = uchwyt.read()
        print(dane)

    def update_file(text_data):
        uchwyt = open('plik2.txt', 'w', encoding='utf-8')
        uchwyt.write(text_data)
        uchwyt.close()

