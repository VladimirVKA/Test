# создать класс, два поля интренал, прайвeд и проперти к прайвд
# залить на репозиторий
class gg:
    __name: str
    _surname:str
    def __init__(self):
        self.__name = ''
        self._surname = ''


    @property
    def getname(self):
        return self.__name
    @getname.setter
    def getname(self, name = 'Ivan'):
        self.__name = name

    @property
    def getsurname(self):
        return self._surname
    def gersurname(self, sername = 'Ivanov'):
        self._surname = sername

if __name__ == '__main__':
    x = gg()


