# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:06:13 2020

@author: sunny
"""

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.44.134',
    'username': 'sn277281',
    'password': 'cisco',
    'secret': 'welcome',
    'blocking_timeout': 16,
}


net_connect = ConnectHandler(**iosv_l2)
net_connect.enable()
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = "isp_air_config"
output = net_connect.send_config_from_file(config_commands)
print(output)