"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    answers = {
    'Приветики!': 'Привет',
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Пргораммирую',
    'Как успехи?': 'Потихоньку'
}
    while True:
        user_question = input('Введите Ваш вопрос: ')
        if user_question in answers.keys():
            print('Программа', answers[user_question])
        else:
            print('Такого вопроса нет в словаре')
    

    
if __name__ == "__main__":
    ask_user()
