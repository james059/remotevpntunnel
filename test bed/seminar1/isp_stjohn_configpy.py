# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:06:13 2020

@author: sunny
"""

from netmiko import ConnectHandler
from isp_snow_configpy import iosv_l2

iosv_head = {
    'device_type': 'cisco_ios',
    'ip': '7.0.0.6',
    'username': 'sn277281',
    'password': 'cisco',
    'secret': 'welcome',
    'blocking_timeout': 16,
}


net_connect = ConnectHandler(**isp_snow_configpy.iosv_l2)
net_connect.enable()
#net_connect.find_prompt()
net_connectsj=ConnectHandler(iosv_head)

config_commands = "isp_stjohn_config"
output = net_connect.send_config_from_file(config_commands)
print(output)