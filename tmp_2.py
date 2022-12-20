import platform
from datetime import datetime

login = {'Стандартный': 'standard_user',
         'Заблокированный': 'locked_out_user',
         'Проблемный': 'problem_user',
         'Ожидание входа': 'performance_glitch_user'}

#for i in login:
#    print(login.get(i))
a = list(login.keys())[0]
print(a)

today_date = datetime.now().date().strftime('%d-%m-%Y')
today_date_string = str(today_date.replace('-', ''))

print(today_date_string)
print(datetime.now())

one_string_address = 'Московская область, город Клин, город Высоковск, улица Ленина, д. 19, кв. 10'
b = one_string_address.split(', ')
print(b)

pay_method = {'Оплата со счета': '1',
              'Оплата по QR': '2',
              'Оплата банковской картой': '3'}

c = list(pay_method.items())
print(c)
#if c == '1':
#    print('Верно')

print(platform.system(), platform.release())
print(platform.platform())
print(platform.system() + ' ' + platform.release())
print(platform.machine())







