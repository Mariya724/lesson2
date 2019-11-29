"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
students_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
                 {'school_class': '4b','scores': [5,5,4,4,5]}]

scores_sum = 0
school_sum = []
for each in students_scores:
   sum_in_class = 0
   for value in each['scores']:
    sum_in_class += value
    value_in_class=int(value)
    school_sum.append(value_in_class)
   print('Средний балл по классу: ', each['school_class'], sum_in_class/len(each['scores']))
scores_sum = sum(school_sum)/len(school_sum)
print('Средний балл по школе: ' , scores_sum)


if __name__ == "__main__":
    main()
