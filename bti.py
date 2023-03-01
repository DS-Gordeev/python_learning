import requests

error_list = []
for i in range(9501, 9867):
    try:
        url = f'https://mosgorbti.com/get-order-info/{i}/'
        req = requests.request('GET', url, timeout=60.0)
        full_text = req.text
        full_text = full_text.replace("\n", "")
        full_text = " ".join(full_text.split())
        # print(full_text)
        # Адрес
        addr_1 = full_text.rfind('Адрес объекта')
        addr_2 = full_text.rfind('</span> </td> </tr> <tr> <td class="txtBold"> <label>Список объектов</label>')
        # Номер квартиры
        flat_1 = full_text.rfind('Список объектов')
        flat_2 = full_text.rfind('</span> </td> </tr> <tr> <td colspan="2">')

        part_1 = full_text[addr_1 + 39:addr_2 - 1]
        part_1 = part_1.replace('/', '-')
        part_2 = full_text[flat_1 + 42:flat_2 - 1]
        part_2 = part_2.replace('№', ' кв.').replace('/', '-')

        full_address = part_1 + part_2

        url = f'https://mosgorbti.com/get-order-info/pdf/{i}/'
        req = requests.request('GET', url, timeout=60.0)
        with open(fr'C:\AutoTests_home\autotests_python\downloadedFiles\{i}-{full_address}.pdf', 'wb') as f:
            f.write(req.content)
        print(f'Заявление {i} - OK!')
    except Exception as error:
        print(f'Для заказа {i} возникла ошибка {error}')
        error_list.append(i)
        continue
print(f'Список заявлений в которых возникла ошибка: {error_list}')








