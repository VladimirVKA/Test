# создать класс, два поля интренал, прайвeд и проперти к прайвд
# залить на репозиторий
class gg:

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

    @getsurname.setter
    def getsurname(self, surname = 'Ivanov'):
        self._surname = surname

if __name__ == '__main__':
    x = gg()
    x.getname = 'Misha'
    x.getsurname = 'Mihailov'
    print(x.getname)
    print(x.getsurname)