class Restaurant:
    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError
        self.__name = None
        self.__name = name

    def get_name(self):
        return self.__name