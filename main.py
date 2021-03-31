from platform import system
import threading
import time
import re
from os import popen

ver = 0.2
server_list = [
    {'ip': 'login.p1.worldoftanks.net', 'name': 'RU1'},
    {'ip': 'login.p2.worldoftanks.net', 'name': 'RU2'},
    {'ip': '192.168.1.76', 'name': 'Test'},
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
            flag = '-n' if system().lower()=='windows' else '-c'
            ping = popen(f"ping {flag} 1 {self.ip}").read()
            ping = re.findall('Average = \d{1,100}',ping)
        else:
            ping = popen(f"ping {self.ip}").read()
            ping = re.findall('Average = \d{1,100}',ping)
        if ping == []:
            result = 'fail'
        else:
            result = ping[0][10:]
        self.result_print(result)
        return result

    def result_print(self,ping):
        if ping == 'fail':
            print(f"{self.name} - {self.ip} is DOWN.")
        else:
            print(f"{self.name} - {self.ip} is UP. Ping = {ping}ms")


    def ping_executor(self):
        while self.auto_check:
            ping = self.ping_me()
            print(ping)
            time.sleep(self.interval)
        self.ping_me()

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
