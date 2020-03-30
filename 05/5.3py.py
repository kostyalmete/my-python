out_interface = input('Введите режим работы интерфейса (trunk/access): ')
out_type = input('Введите тип и номер интерфейса: ')
out_vlan = input('Введите номер влан(ов): ')

access_out = '''
    interface {inter}
    switchport mode access
    switchport access vlan {vlan}
    switchport nonegotiate
    spanning-tree portfast
    spanning-tree bpduguard enable
    '''

trunk_out = '''
    interface {inter}
    switchport trunk encapsulation dot1q
    switchport mode trunk
    switchport trunk allowed vlan {vlan}
    '''


#TRUNK
trunk_user = trunk_out.format(inter=out_type, vlan=out_vlan)
#ACCESS
access_user = access_out.format(inter=out_type, vlan=out_vlan)

#OUT

if out_interface == 'trunk':
    print(trunk_user)
elif out_interface == 'access':
    print(access_user)
else:
    print('-' * 10)
    print('Неправильный режим работы интерфейса')
