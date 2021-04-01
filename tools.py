from platform import system
import threading
from time import sleep
from re import findall
from os import popen

class LackOfData(Exception):
    def __init__(self,arg):
        self.arg = arg
        self.message = 'argument is required!'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.arg} {self.message}'

class Tools:

    def __init__(self,data_controller):
        self.ip = data_controller.ip
        self.name = data_controller.name
        self.ip = data_controller.ip

    @staticmethod
    def ping_me(ip,single_mode):
        if single_mode:
            flag = '-n' if system().lower() == 'windows' else '-c'
            ping = popen(f"ping {flag} 1 {ip}").read()
            ping = findall('Average = \d{1,100}', ping)
        else:
            ping = popen(f"ping {ip}").read()
            ping = findall('Average = \d{1,100}', ping)
        if ping == []:
            result = False
        else:
            result = ping[0][10:]
        return result