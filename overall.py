import json
import datetime


OPEN_HOURS = 10
CLOSE_HOURS = 21


def check_date(func):
    if type(func) == str:
        func = func.split('-')
    if len(func) != 3:
        return False
    if len(func[0]) == 4 and len(func[1]) == 2 and len(func[2]) == 2:
        if func[0].isdigit() and func[1].isdigit() and func[2].isdigit():
            if 2000 <= int(func[0]) <= 3000 and 1 <= int(func[1]) <= 12 and 1 <= int(func[2]) <= 31:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def ask_date():
    date = input()
    while not check_date(date):
        print('Не является датой')
        date = input('Пожалуйста, введите дату вашего посещения МФЦ в формате ГГГГ-ММ-ДД:\n')
        continue
    else:
        return date


def count_numbers(number_list):
    return {x: number_list.count(x) for x in number_list if x}


def sorted_values(func):
    return {x: func.count(x) for x in sorted(func, key=count_numbers(func).get)}


def load_info():
    with open('form.json') as form_:
        info = json.load(form_)
    return info


def compare_dates(a, b, c):
    return datetime.date.fromisoformat(a) <= datetime.date.fromisoformat(b) <= datetime.date.fromisoformat(c)


def average_wait_hours(stat):
    hours = 0
    for elm in stat:
        hours += int(elm['queue wait time'])

    print('Среднее время ожидания: %.2f ч.' % (hours / len(stat)))


def calc_optimization(stat):
    A = [int(record['hour']) for record in stat]
    print('Часы работы от наименьшей загруженности до наибольшей')
    for hour, workload in list(sorted_values(A).items()):
        print(f'{hour}:00 - {workload} человек')


def calc_productivity(stat, date_begin, date_end):
    count = 0
    for record in stat:
        if compare_dates(date_begin, record['date'], date_end):
            count += 1
    print(f'Оказано услуг за выбранный период: {count}')


def main():
    stat = load_info()

    average_wait_hours(stat)

    calc_optimization(stat)

    print('Введите начало временного периода:')
    date_begin = ask_date()

    print('Введите конец временного периода:')
    date_end = ask_date()

    calc_productivity(stat, date_begin, date_end)


main()
