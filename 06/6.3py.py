access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

trunk_template_mod = [
    ' switchport trunk encapsulation dot1q', '\n', 
    'switchport mode trunk'
]
trunk_template_mod = ' '.join(trunk_template_mod)
        
c_add = 'add'
c_del = 'del'
c_only = 'only'


print('\n', '#' * 40, '\n')


for tport, tlist in trunk.items(): 
    vlanlist = [] 
    print('inteface', tport) 
    for vlan in tlist: 
        str(vlan) 
        if vlan.isdigit() == True: 
            vlanlist.append(vlan) 
        else: 
            None 
    vlanlist = ' '.join(vlanlist) 
    for do in tlist:  
        if do.isdigit() == False:  
            dolist = do 
        else:  
            None  
    for command in trunk_template:  
        if command.endswith('allowed vlan'):  
            print(' {} {} {}'.format(command, dolist, vlanlist)) 
        else: 
            print(' {}'.format(command))
