# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:40:17 2020

@author: Vikranth Bari
"""


import subprocess

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
a = [i.split(':')[1][1:-1] for i in a if "All User Profile" in i]

for i in a:
    res = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    res = [b.split(':')[1][1:-1] for b in res if "Key Content" in b]
    
    try:
        print('{:<30}| {:<}'.format(i, res[0]))
    except IndexError:
        print('{:<30}| {:<}'.format(i, ''))