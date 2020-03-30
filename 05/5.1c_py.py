london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
list_r1 = list(london_co['r1'])
list_r2 = list(london_co['r2'])
list_sw1 = list(london_co['sw1'])


ans1 = input('имя интерфейса: ')
#ans2 = input('имя параметра: ')



#R1

if ans1 == 'r1':
    print('Доступные парамерты', list_r1)
    ans2 = input('Введите имя параметра: ')
    if ans2 == 'location':
        print('\n', london_co['r1']['location'])
    elif ans2 == 'vendor':
        print('\n', london_co['r1']['vendor'])
    elif ans2 == 'model':
        print('\n', london_co['r1']['model'])
    elif ans2 == 'ios':
        print('\n', london_co['r1']['ios'])
    elif ans2 == 'ip':
        print('\n', london_co['r1']['ip'])
    else:
        print('-' * 10)
        print('Такого параметра нет')
#R2

if ans1 == 'r2':
    print('Доступные парамерты', list_r2)
    ans2 = input('Введите имя параметра: ')
    if ans2 == 'location':
        print('\n', london_co['r2']['location'])
    elif ans2 == 'vendor':
        print('\n', london_co['r2']['vendor'])
    elif ans2 == 'model':
        print('\n', london_co['r2']['model'])
        print('\n', london_co['r2']['model'])
    elif ans2 == 'ios':
        print('\n', london_co['r2']['ios'])
    elif ans2 == 'ip':
        print('\n', london_co['r2']['ip'])
    else:
        print('-' * 10)
        print('Такого параметра нет')

#SW1

if ans1 == 'sw1':
    print('Доступные парамерты', list_sw1)
    ans2 = input('Введите имя параметра: ')
    if ans2 == 'location':
        print('\n', london_co['sw1']['location'])
    elif ans2 == 'vendor':
        print('\n', london_co['sw1']['vendor'])
    elif ans2 == 'model':
        print('\n', london_co['sw1']['model'])
    elif ans2 == 'ios':
        print('\n', london_co['sw1']['ios'])
    elif ans2 == 'ip':
        print('\n', london_co['sw1']['ip'])
    elif ans2 == 'vlans':
        print('\n', london_co['sw1']['vlans'])
    elif ans2 == 'routing':
        print('\n', london_co['sw1']['routing'])
    else:
        print('-' * 10)
        print('Такого параметра нет')
