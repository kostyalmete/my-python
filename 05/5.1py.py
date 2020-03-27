#!/usr/bin/env python

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

out = input('Ведите имя интерфейса: ')

if out == 'r1':
    print('-' * 10)
    print(london_co['r1'])
elif out == 'r2':
    print(london_co['r2'])
elif out == 'sw1':
    print('-' * 10)
    print(london_co['sw1'])
else:
    print('-' * 10)
    print('Такого имени не существует')
