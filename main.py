from os import popen

ver = 0.1
server_list = [
    {'ip':'8.8.8.8','name':'GOOGLE.com'},
    {'ip':'8.8.4.4','name':'Google.com'},
]

class WOTServer:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.interval = 30000
        self.auto_check = False

    def ping_me(self):
        ping = popen(f"ping {self.ip}").read()
        if "Received = 4" in ping:
            print(f"{self.name} - {self.ip} is UP")
        else:
            print(f"{self.name} - {self.ip} is DOWN")


def main():
    print('WOTping start')
    for server in server_list:
        ip  =server['ip']
        name  =server['name']
        name = WOTServer(ip,name)
        name.ping_me()
    return True


if __name__ == '__main__':
    main()
