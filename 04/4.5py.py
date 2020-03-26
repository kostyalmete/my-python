command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1 = command1.split()
command2 = command2.split()

command1 = command1[4]
command2 = command2[4]

command1 = command1.split(',')
command2 = command2.split(',')

command1 = set(command1)
command2 = set(command2)

command3 = set.intersection(command1, command2)

command3 = list(command3)

command3 = sorted(command3)
print(command3)
