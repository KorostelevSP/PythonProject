# Задача "Найдёт везде":
class WordsFinder:
    def __init__(self,*nameFales):
        self.file_names = nameFales

    def get_all_words(self):
        all_words = {}
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ','\n']
        for name in self.file_names:
            with open(name,encoding='utf-8') as file:
                my_list_global = []
                for line in file:
                    for char in chars_to_remove:
                        line = line.replace(char,"")
                    my_list =  line.split(' ')
                    my_list_global = my_list_global + my_list
            all_words.setdefault(name, my_list_global)
        return all_words

    def find(self,word):
        all_words = finder2.get_all_words()
        my_dct = {}
        for name, words in all_words.items():
            number_words = 0
            for i in range(len(words)):
                if word.lower() == words[i].lower():
                    number_words = (i+1)
                    break
            my_dct.setdefault(name, number_words)
        return my_dct

    def count(self,word):
        all_words = finder2.get_all_words()
        my_dct = {}
        for name, words in all_words.items():
            same_words = 0
            for i in range(len(words)):
                if word.lower() == words[i].lower():
                    same_words +=1
            my_dct.setdefault(name, same_words)
        return my_dct


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
# print(finder2.file_names)
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего