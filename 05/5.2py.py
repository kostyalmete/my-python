#!/usr/bin/env python

out = input('Введите IP/mask -> (10.10.0.0/41): ')

out = out.split('/')

ip = out[0]
mask = out[1]

ip = ip.split('.')

ip1 = int(ip[0])
ip2 = int(ip[1])
ip3 = int(ip[2])
ip4 = int(ip[3])

mask = int(mask)


ip5 = '{:08b}  {:08b}  {:08b} {:08b}'.format(ip1, ip2, ip3, ip4)
mask_format = '{:08b}'.format(mask)

ip = '        '.join(ip)
btw = '-' * 10


ans = '''
Network: 
{ip}

{ip5}

{btw}

mask:
{mask}

{mask_format}
'''


ans_form = ans.format(ip=ip, ip5=ip5, mask=mask, mask_format=mask_format, btw=btw) 


print(ans_form)
