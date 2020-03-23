nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

nat = nat.replace('FastEthernet', 'GigabitEthernet')

print(nat)
