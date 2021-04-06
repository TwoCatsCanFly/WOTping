from platform import system
import threading
from time import sleep
from re import findall
from os import popen
from queue import Queue
from GUI import CLI


class WOTServer:
    def __init__(self, server):
        self.ip = server.get('ip')
        self.name = server.get('name')

    def ping_me(self, mode=True):
        if mode:
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


class Worker:
    def __init__(self, values):
        self.auto_check = values.get('auto_check')
        self.single_mode = values.get('single_mode')
        self.interval = values.get('interval')
        self.server_list = values.get('server_list')
        self.server_data = list()
        self.dialog_queue = Queue()

    def async_executor(self, func, args):
        thread = threading.Thread(target=func, args=[args])
        thread.start()

    def ping_executor(self, server):
        while True:
            result = server.ping_me(self.single_mode)
            self.dialog_queue.put({'ip': server.ip, 'name': server.name, 'ping': result})
            if (self.auto_check == False): break
            sleep(self.interval)

    def stop_auto_check(self):
        self.auto_check = False

    def prep_servers(self):
        for i in self.server_list:
            args = {'ip': i.get('ip'), 'name': i.get('name')}
            self.server_data.append(WOTServer(args))

    def start(self):
        CLI.cli_start(self.dialog_queue, self.auto_check)
        for data in self.server_data:
            self.async_executor(self.ping_executor, data)
