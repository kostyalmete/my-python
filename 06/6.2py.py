user = input('Введите IP адресс: ')
user_split = user.split('.')
user_splitted = []

for inter in user_split:
    user_splitted.append(int(inter))

rangea = list(range(1,224))
rangeb = list(range(224,240))
    
if user_splitted[0] in rangea:
    print('type: unicast')
elif user_splitted[0] in rangeb:
    print('type: multicast')
elif user == '255.255.255.255':
    print('local broadcasting')
elif user == '0.0.0.0':
    print('unassigned') 
else:
    print('unused')
