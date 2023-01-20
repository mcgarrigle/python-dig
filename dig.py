class dig:

    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        return self.__dig_this(self.value[name])

    def __getitem__(self, index):
        return self.__dig_this(self.value[index])

    def __dig_this(self, value):
        if type(value) is dict:
            return dig(value)
        if type(value) is list:
            return dig(value)
        return value

    @property
    def _value(self):
        return self.value
