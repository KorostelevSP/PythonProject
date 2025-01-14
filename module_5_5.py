# "Классы и объекты."
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self):
        return f'Пользователь: {self.nickname}'

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for us in self.users:
            if nickname == us.nickname:
                if hash(password) == us.password:
                    self.current_user = us

    def register(self,nickname, password, age):
        CreateUser = True
        for us in self.users:
            if nickname == us.nickname:
                CreateUser = False

        if CreateUser:
            password_H = hash(password)
            New_Us = User(nickname,password_H,age)
            self.users.append(New_Us)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *other):

        my_other = other
        for val in my_other:
            if not isinstance(val, Video):
                raise ArithmeticError("Правый операнд должен объектом Video")

            CreateVideo = True
            for vid in self.videos:
                if val.title == vid.title:
                    CreateVideo = False

            if CreateVideo:
                self.videos.append(val)

    def get_videos(self,search_word):
        listVideo = []
        for vid in self.videos:
            if search_word.lower() in vid.title.lower():
                listVideo.append(vid.title)
        return listVideo

    def watch_video(self,NameVidos):
        VideoFound = False
        for vid in self.videos:
            if NameVidos == vid.title:
                VideoFound = True
                ourVidos = vid

        if VideoFound:
            if self.current_user == None:
                print(f'Войдите в аккаунт, чтобы смотреть видео')
            elif  getattr(self.current_user, 'age') < 18:
                print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print(f'Запуск видео')
                for i in range(1, getattr(ourVidos, 'duration')+1):
                    print(i)
                    time.sleep(1)
                print(f'Конец видео')
        else:
            print(f'Видео не найдено!: {NameVidos}')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')