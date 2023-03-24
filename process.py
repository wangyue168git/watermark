from multiprocessing import Manager, Pool
import multiprocessing
import os


def add(para):
    para.append(1)
    print(para)
    return para


def worker():
    pass


class Test:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      self.pool = Pool(4)

    def name1(self,name):
      self.name = name
      print(self.name)
      return self.name

    def process(self):
        return self.pool.map(self.name1,["a"])

if __name__ == '__main__':
    test = Test("w",12)
    name = test.process()
    print(name)


