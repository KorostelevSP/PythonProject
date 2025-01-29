# Задача "Найдёт везде":

class WordsFinder:
    def __init__(self,*nameFales):
        self.file_names = nameFales

    def get_all_words(self):
        all_words = {}
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name,encoding='utf-8') as file:
                for line in file:
                    for char in chars_to_remove:
                        line = line.replace(char,"")
                    my_list =  line.split(' ')
                    print(my_list)

finder2 = WordsFinder('test_file.txt')
finder2.get_all_words()
# print(finder2.file_names)