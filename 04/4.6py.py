ospf_route = 'OSPF, 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.split()

ospf_route_form = '''
Protocol:               {PRO}
Prefix:                 {PRE}
AD/Metric:              {ADM}
Next-Hop:               {NH}
Last update:            {LU}
Outbound Interface:     {OI}
'''

ospf_route_format1 = ospf_route_form.format(PRO='OSPF', PRE='10.0.24.0/24', ADM='110/41', NH='10.0.13.3', LU='3d18h', OI='FastEthernet0/0')

print(ospf_route_format1) 
