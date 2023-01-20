import pprint

class dig:

    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        return self.__value(self.value[name])

    def __getitem__(self, index):
        return self.__value(self.value[index])

    def __value(self, value):
        if type(value) is dict:
            return dig(value)
        if type(value) is list:
            return [ self.__value(i) for i in value ]
        return value

s = { "a":1, 
      "b": { "b1": 20, "b2": 21 },
      "c": [ 30, 31, 32 ],
      "d": { "d1": [ { "d11" : 41 }, { "d12": 42 } ] }
    }

def example(s):
  r = eval(s)
  print(s," ",r)

pprint.pprint(s)
o = dig(s)

print(o.d.d1[0].d11)

example("o.a")
example("o.b.b1")
example("o.b.b2")
example("o.c[1]")
example("o.d.d1")
example("o.d.d1[0]")
example("o.d.d1[0].d11")
example("o.d.d1[1]")
example("o.d.d1[1].d12")

print("o.c")
for i in o.c:
    print(" ",i)
