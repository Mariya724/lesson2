"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string1,string2):

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    if type(string1) and type(string2) is not str:
        return ('0')
    elif string1 == string2:
        return('1')
    elif string1 != string2 and len(string1)>len(string2):
        return('2')
    elif string1 != string2 and string2 == 'learn':
        return('3')
 

guess = main('мама','мама')
print(guess)
guess = main('бабушка','мама')
print(guess)
guess = main('мама','learn')
print(guess)
guess = main(2,5)
print(guess)

    
