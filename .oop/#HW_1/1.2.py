"""
Представьте, что вы работаете над чат-ботом для диалога с человеком.
Вам необходимо добавить ему возможность правильно выбирать вариант приветствия в зависимости от времени
в текущем часовом поясе и часового пояса собеседника человека.
Напишите класс, определяющий текущий период суток — утро, день, вечер, ночь — для времени в том или ином
часовом поясе.
Подумайте, какие атрибуты должны определяться в классе, а какие в экземпляре.
Добавьте метод для определения периода суток. Метод должен принимать параметр, задающий смещение от текущего
часового пояса.
Подсказка: используйте модуль datetime.
"""
import datetime
import pytz


class Hello:
    zone: str

    def __init__(self, zone: str):
        self.zone = zone
        self.timezone = pytz.timezone(self.zone)
        self.current_time = datetime.datetime.now(self.timezone)
        self.current_time_hm = self.current_time.time()

    # The function determines the type of greeting, depending on the time of day in the timezone
    def greetings(self):
        if self.current_time_hm >= datetime.time(21) or datetime.time(0) <= self.current_time_hm < datetime.time(4):
            return 'Доброй ночи!'
        elif self.current_time_hm >= datetime.time(16):
            return 'Добрый вечер!'
        elif self.current_time_hm >= datetime.time(11):
            return 'Добрый день!'
        elif self.current_time_hm >= datetime.time(4):
            return 'Доброе утро!'


a = Hello('America/New_York')
# a = Hello('Europe/London')
# a = Hello('Europe/Moscow')
# a = Hello('Iran')
# a = Hello('Asia/Bangkok')
print(a.greetings())
