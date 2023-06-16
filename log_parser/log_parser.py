import json
import re
from collections import defaultdict

dict_ip = defaultdict(int)
dict_http_methods = defaultdict(int)
keys = ['ip', 'http_method', 'duration', 'date', 'url']
list_of_dicts = []

with open('access.log', 'r') as f:
    for line in f:
        # Определяем IP адреса
        ip_match = re.search(r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}?)", line)
        dict_ip[ip_match.group('ip')] += 1

        # Определяем методы http запросов
        http_method = re.search(r"(?P<http_method>(POST|GET|PUT|DELETE|HEAD|OPTIONS))", line)
        dict_http_methods[http_method.group('http_method')] += 1

        # Определяем время выполнения запроса, дату и URL
        execute_time = re.search(r"(?P<time>(\d+)$)", line)
        req_date = re.search(r"(?P<date>\[\d+\/\w+\/\d+:\d+:\d+:\d+ \+\d+\])", line)
        url_match = re.search(r"(?P<url>(http:\/\/[^\"]+))", line)

        if url_match is None:
            url = "-"
        else:
            url = url_match.group('url')

        # Формируем значения ключей словаря
        data = [ip_match.group('ip'), http_method.group('http_method'), execute_time.group('time'),
                req_date.group('date'), url]

        # Собираем словарь из полученных данных и добавляем его в список
        dictionary = dict(zip(keys, data))
        list_of_dicts.append(dictionary)

    # Производим сортировки по кол-ву запросов от ip адресов и времени выполнения запроса
    sorted_ip_dict = sorted(dict_ip.items(), key=lambda x: x[1], reverse=True)
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x['duration'], reverse=True)

    # Подсчитываем суммарное кол-во всех запросов
    dict_http_methods['TOTAL_REQUESTS'] = sum(dict_http_methods.values())

# Формируем итоговый словарь с искомыми данными
result_dict = {'top_ips': dict(sorted_ip_dict[:3]),
               'total_stat': dict(dict_http_methods),
               'top_longest': sorted_list_of_dicts[:3]}

# Записываем в файл result.json итоговый результат
with open("result.json", "w") as result_json:
    data = json.dumps(result_dict, indent=4)
    result_json.write(data)

print(json.dumps(result_dict, indent=4))
