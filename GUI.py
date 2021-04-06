import threading

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class WOTpGUI(QMainWindow):
    def __init__(self):
        super(WOTpGUI, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('WOTping')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('First')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('start')
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('WOW')
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = WOTpGUI()
    win.show()
    sys.exit(app.exec_())


#window()

class CLI:

    @staticmethod
    def printer(data):
        if data.get("ping") != False:
            print(f'{data.get("ip")} -- {data.get("name")} -- PING: {data.get("ping")}ms')
        else:
            print(f'{data.get("ip")} -- {data.get("name")} -- DOWN')

    @staticmethod
    def cli(queue,condition):
        while True:
            if queue.empty()==False:
                data = queue.get()
                CLI.printer(data)

    @staticmethod
    def cli_start(queue,condition):
        thread = threading.Thread(target=CLI.cli, args=[queue,condition])
        thread.start()