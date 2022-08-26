import json


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


def check_int(number, begin, end):
    if not number.isdigit():
        return False

    number = int(number)

    return begin <= number <= end


def ask_int(begin, end):
    number = input()
    while number:
        if check_int(number, begin, end):
            return number
        else:
            print('Некорректное число')
            number = input()
            continue


def save_info(info):
    with open('form.json', 'w') as form_:
        json.dump(info, form_)


def load_info():
    with open('form.json') as form_:
        info = json.load(form_)
    return info


def ask_user():
    print('Пожалуйста, введите дату вашего посещения МФЦ в формате ГГГГ-ММ-ДД: ')
    date = ask_date()

    print(f'Пожалуйста, введите время вашего посещения МФЦ (в целых часах от {OPEN_HOURS} до {CLOSE_HOURS}): ')
    hour = ask_int(OPEN_HOURS, CLOSE_HOURS)

    print('Пожалуйста, введите время ожидания в очереди (в часах): ')
    queue_wait_time = ask_int(0, 12)

    return {'queue wait time': queue_wait_time, 'hour': hour, 'date': date}


def main():
    stat = load_info()

    while True:
        stat.append(ask_user())
        questionary = input('Продолжить заполнение анкет? (Да/нет): ')

        if questionary.lower() != 'да':
            break

    save_info(stat)


main()
