"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
        try:
            user_question = input('Введите Ваш вопрос: ')
            if user_question in answers.keys():
                print('Программа', answers[user_question])
            else:
                print('Такого вопроса нет в словаре')
        except  KeyboardInterrupt:
            print ('Пока')
            break
    
if __name__ == "__main__":
    ask_user()
