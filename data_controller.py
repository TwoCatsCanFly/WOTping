from tools import LackOfData

class DataController:
    def __init__(self,**data):
        self.data_checker(data)
        for key,value in data.items():
            self.key = value

    def data_checker(self,data,required = False):
        if required == False:
            self.required = ['ip']
        for argument in self.required:
            if data.get(argument)==None:
                raise LackOfData(argument)