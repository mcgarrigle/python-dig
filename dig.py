class dig:

    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        return self.__dig_this(self.value[name])

    def __getitem__(self, index):
        return self.__dig_this(self.value[index])

    def __dig_this(self, value):
        if isinstance(value, (list, dict)):
            return dig(value)
        return value

    def __repr__(self):
        return f"<dig value={repr(self.value)} >"

    @property
    def _value(self):
        return self.value
