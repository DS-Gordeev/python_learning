login = {'Стандартный': 'standard_user',
         'Заблокированный': 'locked_out_user',
         'Проблемный': 'problem_user',
         'Ожидание входа': 'performance_glitch_user'}

#for i in login:
#    print(login.get(i))
a = list(login.keys())[0]
print(a)
