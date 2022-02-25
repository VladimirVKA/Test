# создать класс, два поля интренал, прайвад и проперти к прайвд
# залить на репозиторий
class gg:
    def __init__(self):
        self._name = ''
        self._sername = ''

    def getname(self, name:str):
        self._name = name
    def getsername(self, sername:str):
        self._sername = sername
    name = property(getname,getsername)
