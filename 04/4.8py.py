
ip = '192.168.3.1'

ip = ip.split('.')
ip1 = ip[0]
ip2 = ip[1]
ip3 = ip[2]
ip4 = ip[3]

ip_format = '{:08b} {:08b} {:08b} {:08b}'.format(192, 168, 3, 1)

ip_form = '''
{ip1}      {ip2}      {ip3}        {ip4}
{ip_format}
'''
ip_form_ans = ip_form.format(ip1=ip1, ip2=ip2, ip3=ip3, ip4=ip4, ip_format=ip_format)

print(ip_form_ans)
