import operator

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def read_user_str():
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def sort_users_by_age():
    data_sort_user = read_user_str()
    data_sort_user.sort(key=operator.itemgetter('age'))
    return data_sort_user


def filter_users_by_age():
    _new_data = sort_users_by_age()
    result_data = []
    for person in _new_data:
        if person['age'] < 10:
            continue
        else:
            result_data.append(person)
    return result_data


if __name__ == '__main__':
    print(filter_users_by_age())