from platform import system
import threading
from time import sleep
from re import findall
from os import popen

ver = 0.3
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


class WOTServer:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.interval = 10
        self.auto_check = False
        self.single_mode = False

    def ping_me(self):
        if self.single_mode:
            flag = '-n' if system().lower() == 'windows' else '-c'
            ping = popen(f"ping {flag} 1 {self.ip}").read()
            ping = findall('Average = \d{1,100}', ping)
        else:
            ping = popen(f"ping {self.ip}").read()
            ping = findall('Average = \d{1,100}', ping)
        if ping == []:
            result = False
        else:
            result = ping[0][10:]
        return result

    def result_print(self, ping):
        if ping == False:
            print(f"{self.name} - {self.ip} is DOWN.")
        else:
            print(f"{self.name} - {self.ip} is UP. Ping = {ping}ms")

    def ping_executor(self):
        while self.auto_check:
            ping = self.ping_me()
            self.result_print(ping)
            sleep(self.interval)
        self.result_print(self.ping_me())

    def async_ping(self):
        thread = threading.Thread(target=self.ping_executor)
        thread.start()


def main():
    print('WOTping start')
    for server in server_list:
        ip = server['ip']
        name = server['name']
        name = WOTServer(ip, name)
        name.async_ping()
    return True


if __name__ == '__main__':
    main()
