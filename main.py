from platform import system
import threading
from time import sleep
from re import findall
from os import popen
from tools import Worker
from GUI import CLI

ver = 0.4
server_list = [
    {'ip': 'login.p1.worldoftanks.net', 'name': 'RU1'},
    {'ip': 'login.p2.worldoftanks.net', 'name': 'RU2'},
    {'ip': 'login.p3.worldoftanks.net', 'name': 'RU3'},
    {'ip': 'login.p4.worldoftanks.net', 'name': 'RU4'},
    {'ip': 'login.p5.worldoftanks.net', 'name': 'RU5'},
    {'ip': 'login.p6.worldoftanks.net', 'name': 'RU6'},
    {'ip': 'login.p7.worldoftanks.net', 'name': 'RU7'},
    {'ip': 'login.p8.worldoftanks.net', 'name': 'RU8'},
    {'ip': 'login.p9.worldoftanks.net', 'name': 'RU9'},
    {'ip': 'login.p10.worldoftanks.net', 'name': 'RU10'},
    {'ip': 'login.p11.worldoftanks.net', 'name': 'RU11'},
    {'ip': 'login.p12.worldoftanks.net', 'name': 'RU12'},
    {'ip': 'login.p1.worldoftanks.eu', 'name': 'EU1'},
    {'ip': 'login.p2.worldoftanks.eu', 'name': 'EU2'},
    {'ip': 'login-p1.worldoftanks.com', 'name': 'US1'},
    {'ip': 'login-p2.worldoftanks.com', 'name': 'US2'},
    {'ip': 'login.cn-n.worldoftanks.cn', 'name': 'CH1'},
    {'ip': 'login.p1.cn-s.worldoftanks.cn', 'name': 'CH2'},
    {'ip': 'login.p2.cn-s.worldoftanks.cn', 'name': 'CH3'},
    {'ip': 'login.p3.cn-s.worldoftanks.cn', 'name': 'CH4'},
    {'ip': 'login.worldoftanks-sea.com', 'name': 'SEA1'},
    {'ip': 'login.worldoftanks.kr', 'name': 'ROK1'},
]

args = {
    'interval' : 10,
    'auto_check' : False,
    'single_mode' : False,
    'server_list': server_list
}

def main():
    print(f'WOT-ping v{ver} started...')
    worker = Worker(args)
    worker.prep_servers()
    worker.start()

if __name__ == '__main__':
    main()
